import { writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { join, basename } from 'node:path';
import { MAPS_DIR } from './config.js';
import type { FileNode } from './scanner.js';
import type { Issue } from './issues.js';

export function ensureDir(dir: string): void {
  if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
}

export function writeStructureMap(
  serviceName: string,
  repoDir: string,
  tree: FileNode,
  fileCounts: Record<string, number>,
  issues: Issue[],
): string {
  ensureDir(MAPS_DIR);
  const slug = basename(repoDir).replace(/[^a-zA-Z0-9]/g, '-').toLowerCase().replace(/-+/g, '-');
  const filePath = join(MAPS_DIR, `${slug}.md`);

  let md = `# Code Structure Map — ${serviceName}\n\n`;
  md += `> Auto-generated: ${new Date().toISOString().slice(0, 10)}\n`;
  md += `> Repository: \`${basename(repoDir)}\`\n\n`;

  // File breakdown
  md += `## File Breakdown\n\n`;
  md += `| Extension | Count |\n|-----------|-------|\n`;
  const sorted = Object.entries(fileCounts).sort((a, b) => b[1] - a[1]);
  for (const [ext, count] of sorted) {
    md += `| ${ext || '(none)'} | ${count} |\n`;
  }

  // Directory tree
  md += `\n## Directory Tree\n\n`;
  md += '```\n';
  renderTree(tree, md, '');
  md += '```\n';

  // Component graph (simplified)
  md += `\n## Component Graph\n\n`;
  md += '```mermaid\n';
  md += 'graph TD\n';
  renderTopDirs(tree, md);
  md += '```\n';

  // Issues
  md += `\n## Issues Found (${issues.length})\n\n`;

  if (issues.length === 0) {
    md += `✅ No issues detected.\n`;
  } else {
    for (const level of ['critical', 'high', 'medium', 'low']) {
      const group = issues.filter(i => i.severity === level);
      if (group.length === 0) continue;
      md += `### ${level.toUpperCase()}\n\n`;
      for (const issue of group) {
        md += `- **${issue.title}**\n`;
        md += `  > ${issue.detail}\n`;
        md += `  > _${issue.path}_\n\n`;
      }
    }
  }

  writeFileSync(filePath, md, 'utf-8');
  return filePath;
}

function renderTree(node: FileNode, md: string, indent: string): void {
  const MAX_DEPTH = 4;
  const depth = indent.length / 2;

  if (depth > MAX_DEPTH) {
    if (node.children) {
      const remaining = countAll(node);
      md += `${indent}└── ... (${remaining} items)\n`;
    }
    return;
  }

  for (let i = 0; i < (node.children || []).length; i++) {
    const child = node.children![i];
    const isLast = i === node.children!.length - 1;
    const prefix = isLast ? '└── ' : '├── ';
    const branch = isLast ? '    ' : '│   ';

    const marker = child.isDir ? '/' : '';
    md += `${indent}${prefix}${child.name}${marker}\n`;

    if (child.children) {
      renderTree(child, md, indent + branch);
    }
  }
}

function countAll(node: FileNode): number {
  let count = 0;
  function walk(n: FileNode) {
    count++;
    if (n.children) for (const c of n.children) walk(c);
  }
  walk(node);
  return count;
}

function renderTopDirs(tree: FileNode, md: string): void {
  const topDirs = (tree.children || []).filter(c => c.isDir).slice(0, 12);
  for (const d of topDirs) {
    const safeName = d.name.replace(/[^a-zA-Z0-9]/g, '_');
    const label = d.name.length > 15 ? d.name.slice(0, 14) + '…' : d.name;
    md += `  ${safeName}["${label}"]\n`;
  }
  md += `\n`;
  for (let i = 0; i < topDirs.length - 1; i++) {
    const from = topDirs[i].name.replace(/[^a-zA-Z0-9]/g, '_');
    const to = topDirs[i + 1].name.replace(/[^a-zA-Z0-9]/g, '_');
    md += `  ${from} --> ${to}\n`;
  }
}

export function writeCleanupScript(repoDir: string, issues: Issue[]): void {
  const slug = basename(repoDir).replace(/[^a-zA-Z0-9]/g, '-').toLowerCase();
  const outDir = join(MAPS_DIR, slug);
  ensureDir(outDir);
  const filePath = join(outDir, 'cleanup-plan.md');

  let md = `# Cleanup Plan — ${basename(repoDir)}\n\n`;
  md += `> Generated: ${new Date().toISOString().slice(0, 10)}\n\n`;

  let phaseNum = 0;

  // Root clutter
  const rootClutter = issues.filter(i => i.category === 'root-clutter');
  if (rootClutter.length > 0) {
    phaseNum++;
    md += `## Phase ${phaseNum}: Organize Root\n\n`;
    for (const issue of rootClutter) {
      md += `- ${issue.title}\n`;
      md += `  → ${issue.detail}\n\n`;
    }
  }

  // Duplicate models
  const doubleModels = issues.filter(i => i.category === 'double-model');
  if (doubleModels.length > 0) {
    phaseNum++;
    md += `## Phase ${phaseNum}: Consolidate Models\n\n`;
    for (const issue of doubleModels) {
      md += `- ${issue.title}\n`;
      md += `  → ${issue.detail}\n\n`;
    }
  }

  // Flat tests
  const flatTests = issues.filter(i => i.category === 'flat-testing');
  if (flatTests.length > 0) {
    phaseNum++;
    md += `## Phase ${phaseNum}: Organize Tests\n\n`;
    for (const issue of flatTests) {
      md += `- ${issue.title}\n`;
      md += `  → ${issue.detail}\n\n`;
    }
  }

  // Stale migrations
  const staleMigrations = issues.filter(i => i.category === 'stale-migration');
  if (staleMigrations.length > 0) {
    phaseNum++;
    md += `## Phase ${phaseNum}: Clean Migrations\n\n`;
    for (const issue of staleMigrations) {
      md += `- ${issue.title}\n`;
      md += `  → ${issue.detail}\n\n`;
    }
  }

  if (phaseNum === 0) {
    md += `No issues requiring a cleanup plan.\n`;
  }

  writeFileSync(filePath, md, 'utf-8');
}
