#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1" -w "%{http_code}"
