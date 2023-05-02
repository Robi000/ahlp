#!/usr/bin/python3
"""
this module will add header and send request
"""
import urllib.request
from sys import argv


def main():
    """
    the main will be the function to execute
    """
    url = argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
