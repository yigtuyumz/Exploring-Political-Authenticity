#!/usr/bin/env bash

find . -path './.venv' -prune -o -name '__pycache__' -type d -print -exec rm -rf {} \+
