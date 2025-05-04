#!/bin/bash
# Convenience wrapper that mirrors the Node CLI.
# Ensures `.venv` is ready and then calls `logistica-ribt`.

set -e
npm install --silent
logistica-ribt "$1"
