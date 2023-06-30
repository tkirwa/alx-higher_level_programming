#!/bin/bash
# Sends a GET request to a URL and displays the body of the response (if status code is 200)

curl -sL -w "%{http_code}" "$1" -o /tmp/body | tail -n 1 | grep -q 200 && cat /tmp/body
