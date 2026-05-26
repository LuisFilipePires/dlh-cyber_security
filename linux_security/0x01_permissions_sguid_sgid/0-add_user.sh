#!/bin/bash
sudo useradd "$1"
sudo passwd "$1" "$2"
