#!/bin/bash

HASH="${1#\{xor\}}"

python3 -c '
import base64

data = "'"$HASH"'"

decoded = base64.b64decode(data)

key = [0x5f]

result = bytes(
    decoded[i] ^ key[i % len(key)]
    for i in range(len(decoded))
)

print(result.decode())
'
