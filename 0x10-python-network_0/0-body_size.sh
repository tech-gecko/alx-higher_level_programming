#!/bin/bash
# Use curl to get the size of the response body in bytes.
curl -s -o /dev/null -w '%{size_download}' "$1"
