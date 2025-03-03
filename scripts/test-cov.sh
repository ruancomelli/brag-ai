#!/bin/bash

uv run --group test-cov pytest \
    --cov \
    --cov-report=xml \
    --cov-fail-under=100
