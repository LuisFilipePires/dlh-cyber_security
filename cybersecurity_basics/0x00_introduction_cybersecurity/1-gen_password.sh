#!/bin/bash
tr -cd '[:alnum:]' </dev/random | head -c"$1"
