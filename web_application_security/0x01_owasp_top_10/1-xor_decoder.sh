#!/bin/bash
HASH="${1#\{xor\}}"

echo "$HASH" | base64 -d | python3 -c '
