import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { SYNC_STATE_PATH } from './config.js';
import type { SyncState } from './types.js';

export function loadState(): SyncState {
  if (!existsSync(SYNC_STATE_PATH)) {
    return { lastRun: '', lastCommitPerRepo: {} };
  }
  try {
    return JSON.parse(readFileSync(SYNC_STATE_PATH, 'utf-8'));
  } catch {
    return { lastRun: '', lastCommitPerRepo: {} };
  }
}

export function saveState(state: SyncState): void {
  state.lastRun = new Date().toISOString();
  writeFileSync(SYNC_STATE_PATH, JSON.stringify(state, null, 2), 'utf-8');
}
