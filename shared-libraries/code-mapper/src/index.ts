import { join, basename } from 'node:path';
import { existsSync, readdirSync } from 'node:fs';
import { ROOT } from './config.js';
import { walkDir, countFilesByExt, type FileNode } from './scanner.js';
import { detectIssues } from './issues.js';
import { writeStructureMap, writeCleanupScript, ensureDir } from './writer.js';
import { MAPS_DIR } from './config.js';

function guessServiceName(dirName: string): string {
  return dirName
    .replace(/^TrueVow[-_]?/i, '')
    .replace(/^2025[-_]?/i, '')
    .replace(/[-_]/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase())
    .trim();
}

function findServiceDir(name: string): string | null {
  const entries = readdirSync(ROOT, { withFileTypes: true });
  for (const e of entries) {
    if (!e.isDirectory()) continue;
    if (e.name.toLowerCase().includes(name.toLowerCase().replace(/\s+/g, '_'))) return join(ROOT, e.name);
    if (e.name.toLowerCase().includes(name.toLowerCase().replace(/\s+/g, '-'))) return join(ROOT, e.name);
  }
  return null;
}

function main() {
  const targetArg = process.argv[2];
  const targets: string[] = [];

  if (targetArg) {
    targets.push(targetArg);
  } else {
    // Default: map ALL services
    const allDirs = readdirSync(ROOT, { withFileTypes: true });
    const skip = new Set(['SIMLINKS', 'shared-libraries', 'TrueVow_Knowledge', 'TrueVow-Documentation', 'TrueVow_Documentation']);
    for (const d of allDirs) {
      if (d.isDirectory() && !d.name.startsWith('.') && !skip.has(d.name)) {
        targets.push(d.name);
      }
    }
  }

  ensureDir(MAPS_DIR);
  console.log('🔬 code-mapper — structural analysis\n');

  for (const target of targets) {
    const repoDir = findServiceDir(target);
    if (!repoDir) {
      console.log(`  ⚠️  "${target}" not found\n`);
      continue;
    }

    const serviceName = guessServiceName(basename(repoDir));
    console.log(`📂 ${serviceName}`);
    console.log(`   ${repoDir}\n`);

    // Phase 1: Walk
    console.log('   📋 Scanning directory tree...');
    const tree = walkDir(repoDir);
    const fileCounts = countFilesByExt(tree);
    const totalFiles = Object.values(fileCounts).reduce((a, b) => a + b, 0);
    console.log(`   ${totalFiles} files, ${countDirs(tree)} directories\n`);

    // Phase 2: Detect issues
    console.log('   🔍 Detecting issues...');
    const issues = detectIssues(repoDir, tree);
    console.log(`   ${issues.length} issues found\n`);

    // Phase 3: Write output
    const mapPath = writeStructureMap(serviceName, repoDir, tree, fileCounts, issues);
    console.log(`   ✅ Map: ${mapPath}`);

    if (issues.length > 0) {
      writeCleanupScript(repoDir, issues);
      console.log(`   ✅ Cleanup plan: ${MAPS_DIR}\\${basename(repoDir).replace(/[^a-zA-Z0-9]/g, '-').toLowerCase()}\\cleanup-plan.md`);
    }

    console.log();
  }

  console.log('✅ Done. Open TrueVow_Knowledge/Code-Maps/ in Obsidian.');
}

function countDirs(node: FileNode): number {
  let count = 0;
  function walk(n: FileNode) {
    if (n.isDir) count++;
    if (n.children) for (const c of n.children) walk(c);
  }
  walk(node);
  return count - 1; // subtract root
}

main();
