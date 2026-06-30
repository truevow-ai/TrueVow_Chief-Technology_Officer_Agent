import { join } from 'node:path';
import { ROOT } from './config.js';
import { loadState, saveState } from './state.js';
import { scanServices, getGitLog } from './scanner.js';
import {
  writeRepoMap,
  writeServicePages,
  writeDailyActivitySummary,
} from './writer.js';
import type { GitCommit } from './types.js';

function main() {
  console.log('🔍 knowledge-sync — scanning ecosystem\n');

  const state = loadState();
  console.log(`  Last run: ${state.lastRun || 'never'}\n`);

  // Phase 1: Scan all services
  console.log('📦 Scanning services...');
  const services = scanServices();
  const gitRepos = services.filter(s => s.isGitRepo);
  console.log(`  Found ${services.length} services (${gitRepos.length} with git)\n`);

  // Phase 2: Git extraction (since last run)
  console.log('📜 Pulling git logs...');
  const allCommits = new Map<string, GitCommit[]>();
  let newCommitCount = 0;

  for (const service of services) {
    if (!service.isGitRepo) continue;
    const dir = join(ROOT, service.dirName);
    const lastHash = state.lastCommitPerRepo[service.dirName] || state.lastRun || undefined;
    const sinceDate = lastHash ? undefined : (state.lastRun || undefined); // use date if no hash
    const commits = getGitLog(dir, sinceDate);

    if (commits.length > 0) {
      allCommits.set(service.dirName, commits);
      newCommitCount += commits.length;
      // Track latest commit hash for next run
      state.lastCommitPerRepo[service.dirName] = commits[0].hash;
    }
  }
  console.log(`  Found ${newCommitCount} new commit(s)\n`);

  // Phase 3: Write vault
  console.log('📝 Writing vault...');

  writeRepoMap(services);
  writeServicePages(services);

  if (allCommits.size > 0) {
    writeDailyActivitySummary(services, allCommits);
  }

  // Phase 4: Save sync state
  saveState(state);
  console.log(`\n✅ Sync complete — state saved`);
}

main();
