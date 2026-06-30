import { embedQuery } from './embedder.js';
import { search, formatResults, loadIndex } from './store.js';

async function main() {
  const query = process.argv[2];
  if (!query) {
    console.log('Usage: npm run query -- "your search question"');
    console.log('Example: npm run query -- "what DB issues affected platform analytics?"');
    process.exit(1);
  }

  const index = loadIndex();
  if (!index) {
    console.log('No index found. Run `npm run index` first.');
    process.exit(1);
  }

  console.log(`🔍 Searching: "${query}"\n`);

  const queryVector = await embedQuery(query);
  const results = search(queryVector, 5);

  console.log(formatResults(results));
  console.log(`  ${'─'.repeat(60)}`);
  console.log(`  Index: ${index.chunks.length} chunks, ${index.chunks.filter(c => c.type === 'adr').length} ADRs, ${index.chunks.filter(c => c.type === 'incident').length} incidents`);
}

main().catch(err => {
  console.error('❌', err.message);
  process.exit(1);
});
