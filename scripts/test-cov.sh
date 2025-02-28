#!/bin/bash

uv run --group ci nox --session test-cov -- $@
