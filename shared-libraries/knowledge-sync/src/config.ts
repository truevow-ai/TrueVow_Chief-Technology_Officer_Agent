import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

export const ROOT = join(__dirname, '..', '..', '..');
export const KNOWLEDGE_DIR = join(ROOT, 'TrueVow_Knowledge');
export const REPO_MAP_PATH = join(KNOWLEDGE_DIR, 'REPO-MAP.md');
export const SERVICE_DIR = join(KNOWLEDGE_DIR, 'Cross-Service');
export const ADR_DIR = join(KNOWLEDGE_DIR, 'ADRs');
export const SYNC_STATE_PATH = join(KNOWLEDGE_DIR, '.sync-state.json');

export const IGNORED_DIRS = new Set([
  '.git', '.pytest_cache', 'node_modules', '.obsidian',
  'SIMLINKS', 'shared-libraries', 'TrueVow_Knowledge',
  'TrueVow-Documentation', 'TrueVow_Documentation',
]);
