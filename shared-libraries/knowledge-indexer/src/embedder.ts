import { pipeline } from '@xenova/transformers';
import type { Chunk } from './chunker.js';

const MODEL = 'Xenova/all-MiniLM-L6-v2';
const DIMENSIONS = 384;
const MAX_INPUT_LENGTH = 512;

let _extractor: any = null;

async function getExtractor() {
  if (!_extractor) {
    console.log('  Loading embedding model (first download ~80MB)...');
    _extractor = await pipeline('feature-extraction', MODEL);
  }
  return _extractor;
}

export interface Embedding {
  chunk: Chunk;
  vector: number[];
}

function chunkArray<T>(arr: T[], size: number): T[][] {
  const result: T[][] = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  return result;
}

function truncate(text: string): string {
  const words = text.split(/\s+/);
  if (words.length <= MAX_INPUT_LENGTH) return text;
  return words.slice(0, MAX_INPUT_LENGTH).join(' ');
}

export async function embedChunks(chunks: Chunk[]): Promise<Embedding[]> {
  const extractor = await getExtractor();
  const batchSize = 10;
  const batches = chunkArray(chunks, batchSize);
  const results: Embedding[] = [];

  for (let i = 0; i < batches.length; i++) {
    const batch = batches[i];
    const inputs = batch.map(c => truncate(c.content));

    const output = await extractor(inputs, { pooling: 'mean', normalize: true });
    const embeddings = output.tolist();

    for (let j = 0; j < batch.length; j++) {
      results.push({
        chunk: batch[j],
        vector: embeddings[j],
      });
    }

    console.log(`  [${i + 1}/${batches.length}] embedded ${batch.length} chunks`);
  }

  return results;
}

export async function embedQuery(text: string): Promise<number[]> {
  const extractor = await getExtractor();
  const output = await extractor(truncate(text), { pooling: 'mean', normalize: true });
  return output.tolist()[0];
}
