import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

export const ROOT = join(__dirname, '..', '..', '..');
export const KNOWLEDGE_DIR = join(ROOT, 'TrueVow_Knowledge');
export const INDEX_PATH = join(KNOWLEDGE_DIR, '.vector-index.json');
