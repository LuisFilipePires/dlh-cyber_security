#!/bin/bash
SENHA=$(< /dev/urandom tr -cd '[:alnum:]' | head -c"$1")
echo $SENHA
