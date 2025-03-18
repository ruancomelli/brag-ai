#!/bin/bash

uv run --group pre-commit pre-commit run --all-files --show-diff-on-failure
