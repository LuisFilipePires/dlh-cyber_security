#!/bin/bash
sudo addgroup "$1"
sudo chgrp "$1" "$2"
sudo chmod g+rw "$2"
