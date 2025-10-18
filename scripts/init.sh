#!/bin/bash

uv sync --all-groups
uv run --group pre-commit prek install --install-hooks
