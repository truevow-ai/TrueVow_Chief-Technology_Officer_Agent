import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { INDEX_PATH } from './config.js';
import type { Chunk } from './chunker.js';
import type { Embedding } from './embedder.js';

export interface IndexData {
  version: number;
  indexedAt: string;
  chunks: {
    id: string;
    sourceFile: string;
    service: string;
    type: string;
    heading: string;
    content: string;
  }[];
  vectors: number[][];
}

export function saveIndex(embeddings: Embedding[]): void {
  const data: IndexData = {
    version: 1,
    indexedAt: new Date().toISOString(),
    chunks: embeddings.map(e => ({
      id: e.chunk.id,
      sourceFile: e.chunk.sourceFile,
      service: e.chunk.service,
      type: e.chunk.type,
      heading: e.chunk.heading,
      content: e.chunk.content,
    })),
    vectors: embeddings.map(e => e.vector),
  };

  writeFileSync(INDEX_PATH, JSON.stringify(data), 'utf-8');
  console.log(`  ✓ Index saved: ${embeddings.length} chunks, ${INDEX_PATH}`);
}

export function loadIndex(): IndexData | null {
  if (!existsSync(INDEX_PATH)) return null;
  try {
    return JSON.parse(readFileSync(INDEX_PATH, 'utf-8'));
  } catch {
    return null;
  }
}

export function cosineSimilarity(a: number[], b: number[]): number {
  let dot = 0, magA = 0, magB = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    magA += a[i] * a[i];
    magB += b[i] * b[i];
  }
  const denom = Math.sqrt(magA) * Math.sqrt(magB);
  return denom === 0 ? 0 : dot / denom;
}

export interface SearchResult {
  chunk: IndexData['chunks'][0];
  score: number;
}

export function search(queryVector: number[], topK: number = 5): SearchResult[] {
  const index = loadIndex();
  if (!index) return [];

  const scored: SearchResult[] = index.vectors.map((vec, i) => ({
    chunk: index.chunks[i],
    score: cosineSimilarity(queryVector, vec),
  }));

  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, topK);
}

export function formatResults(results: SearchResult[]): string {
  if (results.length === 0) return 'No results found.';

  let output = '';
  for (const r of results) {
    output += `\n[${(r.score * 100).toFixed(1)}%] ${r.chunk.sourceFile} — ${r.chunk.heading}\n`;
    output += `${'─'.repeat(60)}\n`;
    const preview = r.chunk.content.length > 300
      ? r.chunk.content.slice(0, 297) + '...'
      : r.chunk.content;
    output += preview + '\n\n';
  }
  return output;
}
