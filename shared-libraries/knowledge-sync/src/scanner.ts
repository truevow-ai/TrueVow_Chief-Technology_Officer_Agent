import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { execSync, spawnSync } from 'node:child_process';
import { ROOT, IGNORED_DIRS } from './config.js';
import type { ServiceInfo, GitCommit } from './types.js';

function detectStack(dir: string): string {
  if (existsSync(join(dir, 'pyproject.toml'))) return 'Python';
  if (existsSync(join(dir, 'package.json'))) {
    try {
      const pkg = JSON.parse(readFileSync(join(dir, 'package.json'), 'utf-8'));
      const deps = { ...pkg.dependencies, ...pkg.devDependencies };
      if (deps.next) return 'Next.js';
      if (deps.react) return 'React';
      if (deps.express) return 'Express';
      if (deps.fastify) return 'Fastify';
      return 'Node.js';
    } catch {
      return 'Node.js';
    }
  }
  return 'Unknown';
}

function guessServiceName(dirName: string): string {
  return dirName
    .replace(/^TrueVow[-_]?/i, '')
    .replace(/^2025[-_]?/i, '')
    .replace(/[-_]/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase())
    .trim();
}

const KNOWN_PORTS: Record<string, number> = {
  'Platform Analytics': 3071,
  'Internal Ops': 3006,
};

function guessPort(name: string): number | undefined {
  return KNOWN_PORTS[name];
}

export function scanServices(): ServiceInfo[] {
  const entries = readdirSync(ROOT, { withFileTypes: true });
  const services: ServiceInfo[] = [];

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const dirName = entry.name;
    if (IGNORED_DIRS.has(dirName) || dirName.startsWith('.')) continue;

    const dir = join(ROOT, dirName);
    const stack = detectStack(dir);
    const name = guessServiceName(dirName);
    const isGitRepo = existsSync(join(dir, '.git'));

    let description = '';
    let dependencies: string[] = [];
    let commitCount: number | undefined;

    if (stack !== 'Python' && existsSync(join(dir, 'package.json'))) {
      try {
        const pkg = JSON.parse(readFileSync(join(dir, 'package.json'), 'utf-8'));
        description = pkg.description || '';
        dependencies = Object.keys({ ...pkg.dependencies, ...pkg.devDependencies });
      } catch { /* skip */ }
    }

    if (stack === 'Python' && existsSync(join(dir, 'pyproject.toml'))) {
      try {
        const content = readFileSync(join(dir, 'pyproject.toml'), 'utf-8');
        const descMatch = content.match(/description\s*=\s*"([^"]+)"/);
        if (descMatch) description = descMatch[1];
      } catch { /* skip */ }
    }

    if (isGitRepo) {
      try {
        const count = execSync('git rev-list --count HEAD', { cwd: dir, encoding: 'utf-8' }).trim();
        commitCount = parseInt(count, 10);
      } catch { /* skip */ }
    }

    services.push({
      dirName,
      name,
      description,
      stack,
      port: guessPort(name),
      dependencies: dependencies.length > 0 ? dependencies.slice(0, 10) : undefined,
      isGitRepo,
      commitCount,
    });
  }

  services.sort((a, b) => a.name.localeCompare(b.name));
  return services;
}

function runGit(args: string[], dir: string): string {
  const result = spawnSync('git', args, { cwd: dir, encoding: 'utf-8', shell: false });
  if (result.error || result.status !== 0) return '';
  return result.stdout.trim();
}

export function getGitLog(dir: string, since?: string): GitCommit[] {
  if (!existsSync(join(dir, '.git'))) return [];

  const args = ['log', `--format=%H|%an|%ai|%s`];
  if (since) {
    args.push(`--since=${since}`);
  } else {
    args.push('--max-count=30');
  }

  const output = runGit(args, dir);
  if (!output) return [];

  return output.split('\n').map(line => {
    const parts = line.split('|');
    return {
      hash: parts[0],
      author: parts[1],
      date: parts[2],
      message: parts.slice(3).join('|'),
    };
  });
}

export function getChangesSince(dir: string, since?: string): string[] {
  if (!existsSync(join(dir, '.git'))) return [];

  try {
    const firstCommit = runGit(['rev-list', '--max-parents=0', 'HEAD'], dir);
    if (!firstCommit) return [];

    const args = ['diff', '--name-only', firstCommit, 'HEAD'];
    const output = runGit(args, dir);
    return output ? output.split('\n').filter(Boolean) : [];
  } catch {
    return [];
  }
}
