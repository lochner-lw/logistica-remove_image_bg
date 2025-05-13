#!/usr/bin/env node
/**
 * NodeJS CLI wrapper around the Python `main.py` script.
 * Keeps the heavy lifting in Python (rembg / ONNX Runtime)
 * while providing an npm-installable command-line UX.
 */

import fs from 'node:fs';
import path from 'node:path';
import { execa } from 'execa';
import chalk from 'chalk';

async function main() {
  const args = process.argv.slice(2);

  // ── Validate CLI args ──────────────────────────────────────────────────────
  if (args.length < 1) {
    console.log(`Usage: ${chalk.cyan('logistica-ribt <image_path>')}`);
    process.exit(1);
  }

  const inputPath = path.resolve(args[0]);
  if (!fs.existsSync(inputPath)) {
    console.error(chalk.red(`⨯ File does not exist: ${inputPath}`));
    process.exit(1);
  }

  // ── Build paths to Python runtime & script ────────────────────────────────
  const projectRoot = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
  const pythonExe   = path.join(projectRoot, '.venv', 'bin', 'python');
  const scriptPath  = path.join(projectRoot, 'main.py');

  // Quick sanity-check that the venv exists
  if (!fs.existsSync(pythonExe)) {
    console.error(chalk.yellow('Virtual-env not found. Running setup…'));
    await execa('bash', ['install.sh'], { cwd: projectRoot, stdio: 'inherit' });
  }

  // ── Spawn the Python process ──────────────────────────────────────────────
  try {
    await execa(pythonExe, [scriptPath, inputPath], { stdio: 'inherit' });
  } catch (err) {
    console.error(chalk.red('Python script failed:'), err.shortMessage || err);
    process.exit(err.exitCode ?? 1);
  }
}

main();
