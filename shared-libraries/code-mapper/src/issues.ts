import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { join, basename } from 'node:path';
import type { FileNode } from './scanner.js';

export interface Issue {
  severity: 'critical' | 'high' | 'medium' | 'low';
  category: 'dead-code' | 'duplicate' | 'stale-migration' | 'root-clutter' | 'flat-testing' | 'double-model';
  title: string;
  detail: string;
  path: string;
}

export function detectIssues(repoDir: string, tree: FileNode): Issue[] {
  const issues: Issue[] = [];

  issues.push(...detectRootClutter(repoDir, tree));
  issues.push(...detectFlatTestFiles(tree));
  issues.push(...detectStaleMigrations(repoDir));
  issues.push(...detectDuplicateModels(repoDir));
  issues.push(...detectDuplicateFiles(tree));
  issues.push(...detectDeepNesting(tree));
  issues.push(...detectStaleDocs(repoDir));

  return issues;
}

function detectRootClutter(repoDir: string, tree: FileNode): Issue[] {
  const issues: Issue[] = [];
  const rootFiles = (tree.children || []).filter(c => !c.isDir);
  const excessiveTypes = {
    '.bat': 2,
    '.ipynb': 1,
    '.md': 5,
  };

  const counts: Record<string, number> = {};
  for (const f of rootFiles) counts[f.ext] = (counts[f.ext] || 0) + 1;

  for (const [ext, threshold] of Object.entries(excessiveTypes)) {
    if ((counts[ext] || 0) > threshold) {
      issues.push({
        severity: 'medium',
        category: 'root-clutter',
        title: `${counts[ext]} ${ext} files at repository root`,
        detail: `Move to a subfolder (${
          ext === '.md' ? 'docs/' : ext === '.bat' ? 'scripts/' : 'notebooks/'
        })`,
        path: join(repoDir),
      });
    }
  }

  return issues;
}

function detectFlatTestFiles(tree: FileNode): Issue[] {
  const testDirs = findDirs(tree, 'tests', 2);
  const issues: Issue[] = [];

  for (const td of testDirs) {
    const flatTestFiles = (td.children || []).filter(c =>
      !c.isDir && c.ext === '.py' && c.name.startsWith('test_') && !c.name.startsWith('__')
    );
    if (flatTestFiles.length > 20) {
      issues.push({
        severity: 'high',
        category: 'flat-testing',
        title: `${flatTestFiles.length} test files flat in ${td.name}/ — no subfolder organization`,
        detail: 'Group by domain: billing/, voice/, draft/, integration/, etc.',
        path: td.path,
      });
    }
  }
  return issues;
}

function detectStaleMigrations(repoDir: string): Issue[] {
  const issues: Issue[] = [];
  const migrationDirs = [
    [join(repoDir, 'migrations'), 'Alembic'],
    [join(repoDir, 'migrations', 'versions'), 'Alembic versions'],
  ];

  for (const [dir, label] of migrationDirs) {
    if (!existsSync(dir)) continue;
    try {
      const files = readdirSync(dir).filter(f => f.endsWith('.py') && !f.startsWith('__') && !f.startsWith('env'));
      if (files.length > 20) {
        issues.push({
          severity: 'medium',
          category: 'stale-migration',
          title: `${files.length} ${label} migration files — many likely already applied`,
          detail: 'Migrations already applied to production should be archived to prevent confusion.',
          path: dir,
        });
      }
    } catch { /* skip */ }
  }

  const dbDirs = [join(repoDir, 'database'), join(repoDir, 'db')];
  for (const dd of dbDirs) {
    if (!existsSync(dd)) continue;
    if (existsSync(join(repoDir, 'migrations'))) {
      issues.push({
        severity: 'medium',
        category: 'stale-migration',
        title: `Both migrations/ and ${basename(dd)}/ exist — possible dual ORM setup`,
        detail: 'One ORM configuration is likely stale. Review and archive the unused one.',
        path: dd,
      });
    }
  }

  return issues;
}

function detectDuplicateModels(repoDir: string): Issue[] {
  const issues: Issue[] = [];
  const modelDirs: string[] = [];
  const candidates = [join(repoDir, 'models'), join(repoDir, 'app', 'models')];

  for (const d of candidates) {
    if (existsSync(d)) modelDirs.push(d);
  }

  if (modelDirs.length > 1) {
    issues.push({
      severity: 'high',
      category: 'double-model',
      title: 'Multiple models/ directories exist — choose one',
      detail: `${modelDirs.join(', ')} — one is likely stale or shadowing the other.`,
      path: repoDir,
    });
  }

  return issues;
}

function detectDuplicateFiles(tree: FileNode): Issue[] {
  const issues: Issue[] = [];
  const nameMap = new Map<string, string[]>();

  function walk(n: FileNode) {
    if (!n.isDir) {
      const existing = nameMap.get(n.name) || [];
      existing.push(n.path);
      nameMap.set(n.name, existing);
    }
    if (n.children) for (const c of n.children) walk(c);
  }
  walk(tree);

  for (const [name, paths] of nameMap) {
    if (paths.length > 1 && !name.startsWith('__init__') && !name.startsWith('.env')) {
      issues.push({
        severity: 'medium',
        category: 'duplicate',
        title: `"${name}" appears in ${paths.length} locations`,
        detail: `Found at: ${paths.slice(0, 3).join(', ')}${paths.length > 3 ? '...' : ''}`,
        path: paths[0],
      });
    }
  }

  return issues;
}

function detectDeepNesting(tree: FileNode): Issue[] {
  const issues: Issue[] = [];
  const maxDepth = 5;

  function walk(n: FileNode, depth: number) {
    if (depth > maxDepth && n.isDir) {
      issues.push({
        severity: 'low',
        category: 'dead-code',
        title: `Deep nesting (depth ${depth}): ${n.path}`,
        detail: 'Deeply nested folders are hard to discover. Consider flattening.',
        path: n.path,
      });
    }
    if (n.children && depth <= maxDepth + 2) {
      for (const c of n.children) walk(c, depth + 1);
    }
  }
  walk(tree, 0);
  return issues;
}

function detectStaleDocs(repoDir: string): Issue[] {
  const issues: Issue[] = [];
  const docsDir = join(repoDir, 'docs');

  if (!existsSync(docsDir)) return issues;

  try {
    const found = readdirSync(docsDir, { withFileTypes: true });
    for (const f of found) {
      if (f.isDirectory() && (f.name === 'archive' || f.name.startsWith('_'))) {
        issues.push({
          severity: 'low',
          category: 'stale-migration',
          title: `Archive folder found: docs/${f.name}/`,
          detail: 'Archive folders should be outside the repo or explicitly tagged for deletion review.',
          path: join(docsDir, f.name),
        });
      }
    }
  } catch { /* skip */ }

  return issues;
}

function findDirs(node: FileNode, name: string, maxDepth: number): FileNode[] {
  const results: FileNode[] = [];
  function walk(n: FileNode, depth: number) {
    if (n.isDir && n.name === name) { results.push(n); return; }
    if (depth >= maxDepth || !n.children) return;
    for (const c of n.children) walk(c, depth + 1);
  }
  walk(node, 0);
  return results;
}
