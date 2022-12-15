#!/bin/bash
# Bash script that sends a request to a URL and displays body size
curl -so /dev/null -w '%{size_download}\n' "$1"
