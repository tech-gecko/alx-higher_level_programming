#!/bin/env bash

# Use curl to get the size of the response body in bytes.
response_size=$(curl -s -o /dev/null -w '%{size_download}' "$1")
echo $response_size
