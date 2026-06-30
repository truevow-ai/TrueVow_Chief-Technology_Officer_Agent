import { readdirSync, statSync } from 'node:fs';
import { join, relative, basename, extname } from 'node:path';
import { IGNORED_DIRS, IGNORED_EXTENSIONS } from './config.js';

export interface FileNode {
  path: string;
  name: string;
  size: number;
  ext: string;
  isDir: boolean;
  children?: FileNode[];
}

export interface ImportEdge {
  from: string;
  to: string;
  type: 'py-import' | 'py-from' | 'js-import' | 'js-require';
}

export function walkDir(dir: string, depth: number = 0): FileNode {
  const name = basename(dir);
  const relativePath = relative(process.cwd(), dir) || name;
  const node: FileNode = {
    path: relativePath,
    name,
    size: 0,
    ext: '',
    isDir: true,
    children: [],
  };

  let entries;
  try {
    entries = readdirSync(dir, { withFileTypes: true });
  } catch {
    return node;
  }

  for (const entry of entries) {
    if (entry.name.startsWith('.') && entry.name !== '.env.local' && entry.name !== '.env.example') continue;
    if (IGNORED_DIRS.has(entry.name)) continue;

    const fullPath = join(dir, entry.name);

    if (entry.isDirectory()) {
      const child = walkDir(fullPath, depth + 1);
      node.children!.push(child);
      node.size += child.size;
    } else {
      const ext = extname(entry.name).toLowerCase();
      if (IGNORED_EXTENSIONS.has(ext)) continue;

      let size = 0;
      try { size = statSync(fullPath).size; } catch { /* skip */ }

      node.children!.push({
        path: relative(process.cwd(), fullPath),
        name: entry.name,
        size,
        ext,
        isDir: false,
      });
      node.size += size;
    }
  }

  node.children!.sort((a, b) => {
    if (a.isDir !== b.isDir) return a.isDir ? -1 : 1;
    return a.name.localeCompare(b.name);
  });

  return node;
}

export function countFilesByExt(node: FileNode): Record<string, number> {
  const counts: Record<string, number> = {};
  function walk(n: FileNode) {
    if (!n.isDir) {
      counts[n.ext] = (counts[n.ext] || 0) + 1;
    }
    if (n.children) {
      for (const c of n.children) walk(c);
    }
  }
  walk(node);
  return counts;
}

export function flattenCodeFiles(node: FileNode): string[] {
  const files: string[] = [];
  const codeExts = new Set(['.py', '.ts', '.tsx', '.js', '.jsx', '.toml', '.yaml', '.yml', '.json', '.cfg', '.ini']);
  function walk(n: FileNode) {
    if (!n.isDir) {
      if (codeExts.has(n.ext)) files.push(n.path);
    }
    if (n.children) for (const c of n.children) walk(c);
  }
  walk(node);
  return files;
}
