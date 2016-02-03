#!/bin/bash

set -e

target="$1"

printf "\nUsage options: $0  <dev|prod>\n\n"

if [[ -z "$target" ]]; then
  printf "No build target specified, using \"dev\"\n\n"
  target="dev"
fi

if [[ "$target" = "dev" || "$target" = "prod" ]]; then
  printf "Building target: \"$target\"\n\n"
  if [ -z ${DJANGO_SETTINGS_MODULE+x} ]; then
    echo "DJANGO_SETTINGS_MODULE is unset"
    export DJANGO_SETTINGS_MODULE="BloggingDemo.settings.$target"
  fi
fi

echo $DJANGO_SETTINGS_MODULE
