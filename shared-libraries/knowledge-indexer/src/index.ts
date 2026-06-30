import { loadAllChunks } from './chunker.js';
import { embedChunks } from './embedder.js';
import { saveIndex, loadIndex } from './store.js';

async function main() {
  console.log('🧠 knowledge-indexer — building vector index\n');

  // Check if reindex is needed
  const existing = loadIndex();
  if (existing) {
    console.log(`  Existing index: ${existing.chunks.length} chunks from ${existing.indexedAt}`);
    console.log('  Delete .vector-index.json to force reindex\n');
    console.log('✅ Index already exists — run `npm run query` to search');
    return;
  }

  // Phase 1: Chunk all .md files
  console.log('📄 Loading chunks...');
  const chunks = loadAllChunks();
  console.log(`  ${chunks.length} chunks from ${new Set(chunks.map(c => c.sourceFile)).size} files\n`);

  // Phase 2: Embed
  console.log('🔮 Embedding...');
  const embeddings = await embedChunks(chunks);
  console.log();

  // Phase 3: Save
  console.log('💾 Saving index...');
  saveIndex(embeddings);

  console.log('\n✅ Index complete — run `npm run query` to search');
}

main().catch(err => {
  console.error('❌', err.message);
  process.exit(1);
});
