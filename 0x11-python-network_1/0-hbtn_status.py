#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status.
"""

import urllib.request

if __name__ == "__main__":
    """Retrieve and display the body response of the URL."""
    url = "https://alx-intranet.hbtn.io/status"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        """Read the response and display the body response."""
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
