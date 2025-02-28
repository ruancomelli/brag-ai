#!/bin/bash

uv run --group ci nox --session type-check -- $@
