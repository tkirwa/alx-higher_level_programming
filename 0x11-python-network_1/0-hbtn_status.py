#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status.
"""

import urllib.request


if __name__ == "__main__":
    # Create a request object with the URL
    request = urllib.request.Request("https://intranet.hbtn.io/status")

    # Send the request and retrieve the response
    with urllib.request.urlopen(request) as response:
        # Read the response body
        body = response.read()

        # Print the body response
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
