import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';
import { KNOWLEDGE_DIR } from './config.js';

export interface Chunk {
  id: string;
  sourceFile: string;
  service: string;
  type: 'adr' | 'incident' | 'session' | 'service-map' | 'decision' | 'other';
  heading: string;
  content: string;
  tokens: number;
}

function estimateTokens(text: string): number {
  return Math.ceil(text.length / 4);
}

function classifyType(filePath: string): Chunk['type'] {
  const relativePath = relative(KNOWLEDGE_DIR, filePath).toLowerCase();
  if (relativePath.startsWith('adrs')) return 'adr';
  if (relativePath.startsWith('incidents')) return 'incident';
  if (relativePath.startsWith('session-logs')) return 'session';
  if (relativePath.startsWith('cross-service')) return 'service-map';
  if (relativePath.startsWith('decisions')) return 'decision';
  return 'other';
}

function inferService(filePath: string): string {
  const relativePath = relative(KNOWLEDGE_DIR, filePath);
  // Try to find a service name in the path or content
  const parts = relativePath.replace(/\\/g, '/').split('/');
  return parts[0] || 'general';
}

function splitIntoChunks(filePath: string, content: string): Chunk[] {
  const chunks: Chunk[] = [];
  const type = classifyType(filePath);
  const service = inferService(filePath);
  const sourceFile = relative(KNOWLEDGE_DIR, filePath);
  const MAX_TOKENS = 512;
  const lines = content.split('\n');

  let currentHeading = '(no heading)';
  let currentBuffer: string[] = [];
  let currentTokens = 0;
  let chunkIndex = 0;

  function flush() {
    if (currentBuffer.length === 0) return;
    const text = currentBuffer.join('\n').trim();
    if (!text) return;
    const id = `${sourceFile.replace(/[^a-zA-Z0-9]/g, '_')}_${chunkIndex}`;
    chunks.push({
      id,
      sourceFile,
      service,
      type,
      heading: currentHeading,
      content: text,
      tokens: currentTokens,
    });
    chunkIndex++;
  }

  for (const line of lines) {
    const headingMatch = line.match(/^(#{1,3})\s+(.+)/);
    if (headingMatch) {
      const level = headingMatch[1].length;
      if (level <= 2) {
        flush();
        currentHeading = headingMatch[2].trim();
        currentBuffer = [];
        currentTokens = 0;
      }
    }

    const lineTokens = estimateTokens(line);
    if (currentTokens + lineTokens > MAX_TOKENS && currentBuffer.length > 0) {
      flush();
      currentHeading = '(continued)';
      currentBuffer = [];
      currentTokens = 0;
    }

    currentBuffer.push(line);
    currentTokens += lineTokens;
  }

  flush();
  return chunks;
}

export function loadAllChunks(): Chunk[] {
  const allChunks: Chunk[] = [];

  function walkDir(dir: string) {
    const entries = readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        if (entry.name.startsWith('.')) continue;
        if (entry.name === 'Templates') continue;
        walkDir(fullPath);
      } else if (entry.name.endsWith('.md') && entry.name !== 'REPO-MAP.md') {
        const content = readFileSync(fullPath, 'utf-8');
        const chunks = splitIntoChunks(fullPath, content);
        allChunks.push(...chunks);
      }
    }
  }

  walkDir(KNOWLEDGE_DIR);
  return allChunks;
}
