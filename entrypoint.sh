#!/usr/bin/env bash

set -e
set -x

uvicorn main:app --reload --host 0.0.0.0 --port 8000
