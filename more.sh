#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <ip_address>"
    exit 1
fi

IP_ADDRESS="$1"
scp prompts.txt "ubuntu@${IP_ADDRESS}:bark/"
ssh "ubuntu@${IP_ADDRESS}" "cd bark; python run.py"
