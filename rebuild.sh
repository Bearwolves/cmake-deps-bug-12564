#!/bin/bash

SCRIPT=$(readlink -f "$0")
SCRIPT_DIR=$(dirname "$SCRIPT")

rm -rf "$SCRIPT_DIR"/build
./build.sh