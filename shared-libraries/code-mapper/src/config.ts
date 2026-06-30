import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

export const ROOT = join(__dirname, '..', '..', '..');
export const KNOWLEDGE_DIR = join(ROOT, 'TrueVow_Knowledge');
export const MAPS_DIR = join(KNOWLEDGE_DIR, 'Code-Maps');

export const IGNORED_DIRS = new Set([
  '__pycache__', '.git', '.venv', 'node_modules', '.pytest_cache',
  '.cursor', '.qoder', '.vscode', '.next', '.opencode',
  '.agent-rules', '.clinerules', '.credentials', '.github', '.tmp_test',
  'logs', 'data',
]);

export const IGNORED_EXTENSIONS = new Set([
  '.pyc', '.pyo', '.log', '.zip', '.gz', '.tar', '.jpg', '.png',
  '.mp4', '.wav', '.mp3', '.ogg', '.pdf', '.docx', '.xlsx',
  '.onnx', '.bin', '.pkl', '.pickle', '.db', '.sqlite', '.sqlite3',
]);
