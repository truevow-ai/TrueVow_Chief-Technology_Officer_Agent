export interface ServiceInfo {
  dirName: string;
  name: string;
  description: string;
  stack: string;
  port?: number;
  dependencies?: string[];
  isGitRepo: boolean;
  commitCount?: number;
}

export interface GitCommit {
  hash: string;
  author: string;
  date: string;
  message: string;
}

export interface SyncState {
  lastRun: string;
  lastCommitPerRepo: Record<string, string>;
}
