#!/bin/bash
# Sends a request to a URL and displays the size of the response body

# Get the URL from the command-line argument
url=$1

# Send the request and store the response in a variable
response=$(curl -sI "$url")

# Extract the Content-Length header value from the response
content_length=$(echo "$response" | grep -i Content-Length | awk '{print $2}')

# Display the content length (size) in bytes
echo "$content_length"
