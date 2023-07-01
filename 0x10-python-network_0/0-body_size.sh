#!/bin/bash
# This script takes in a URL, send a request to same and displays the size of the body of the response, in bytes.
curl -s "$1" -w "%{size_download}\n" -o /dev/null
