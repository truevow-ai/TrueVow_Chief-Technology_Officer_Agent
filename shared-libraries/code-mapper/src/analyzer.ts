import { readFileSync } from 'node:fs';
import { basename } from 'node:path';
import type { ImportEdge } from './scanner.js';

export function parseImports(filePath: string): ImportEdge[] {
  try {
    const content = readFileSync(filePath, 'utf-8');
    const ext = filePath.split('.').pop()?.toLowerCase();
    const source = filePath;

    if (ext === 'py') return parsePython(source, content);
    if (ext === 'ts' || ext === 'tsx') return parseTS(source, content);
    if (ext === 'js' || ext === 'jsx') return parseJS(source, content);
    return [];
  } catch {
    return [];
  }
}

function parsePython(source: string, content: string): ImportEdge[] {
  const edges: ImportEdge[] = [];
  const lines = content.split('\n');

  for (const line of lines) {
    const stripped = line.trim();
    if (stripped.startsWith('#')) continue;

    const fromMatch = stripped.match(/^from\s+([\w.]+)\s+import\s+(.+)/);
    if (fromMatch) {
      const module = fromMatch[1].split('.')[0];
      edges.push({ from: source, to: module, type: 'py-from' });
      continue;
    }

    const importMatch = stripped.match(/^import\s+(.+)/);
    if (importMatch) {
      const modules = importMatch[1].split(',');
      for (const m of modules) {
        const name = m.trim().split(/\s+as\s+/)[0].trim().split('.')[0];
        edges.push({ from: source, to: name, type: 'py-import' });
      }
    }
  }
  return edges;
}

function parseTS(source: string, content: string): ImportEdge[] {
  const edges: ImportEdge[] = [];
  const lines = content.split('\n');

  for (const line of lines) {
    const stripped = line.trim();

    const esMatch = stripped.match(/import\s+(?:[\w{},*\s]+from\s+)?['"]([^'"]+)['"]/);
    if (esMatch) {
      const module = cleanImport(esMatch[1]);
      edges.push({ from: source, to: module, type: 'js-import' });
      continue;
    }

    const requireMatch = stripped.match(/require\s*\(\s*['"]([^'"]+)['"]\s*\)/);
    if (requireMatch) {
      const module = cleanImport(requireMatch[1]);
      edges.push({ from: source, to: module, type: 'js-require' });
    }
  }
  return edges;
}

function parseJS(source: string, content: string): ImportEdge[] {
  return parseTS(source, content);
}

function cleanImport(path: string): string {
  return path.replace(/^[@]/, '').replace(/^\.\.?\//, '').split('/')[0].split('#')[0];
}
