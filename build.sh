#!/bin/bash

set -e

SCRIPT=$(readlink -f "$0")
SCRIPT_DIR=$(dirname "$SCRIPT")

BUILD_DIR_APP="$SCRIPT_DIR"/build/app
BUILD_DIR_LIBS="$SCRIPT_DIR"/build/libs
SRC_DIR_APP="$SCRIPT_DIR"/app
SRC_DIR_LIBS="$SCRIPT_DIR"/libs

mkdir -p "$SCRIPT_DIR"/build/app
mkdir -p "$SCRIPT_DIR"/build/libs

cd "$BUILD_DIR_LIBS" || exit 1
conan install --profile:host default --profile:build linux-settings --install-folder "$BUILD_DIR_LIBS" "$SRC_DIR_LIBS"
conan build "$SRC_DIR_LIBS"
conan package "$SRC_DIR_LIBS"
conan export-pkg "$SRC_DIR_LIBS" --force


cd "$BUILD_DIR_APP" || exit 1
conan install --profile:host default --profile:build linux-settings --install-folder "$BUILD_DIR_APP" "$SRC_DIR_APP"
conan build "$SRC_DIR_APP"
conan package "$SRC_DIR_APP"
conan export-pkg "$SRC_DIR_APP" --force
