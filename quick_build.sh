#!/usr/bin/env bash
# set -euo pipefail
PROJECT=pyanide
mypy $PROJECT
pylint $PROJECT
pytest test
pytest pyanide --doctest-modules