#!/bin/bash

uv run --group ci nox --session lint -- $@
