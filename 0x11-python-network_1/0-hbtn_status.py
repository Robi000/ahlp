#!/usr/bin/python3
"""
this file will  https://alx-intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    the main function to be executed
    """
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        response_read = response.read()
        print("Body response:")
        print("\t- type:", type(response_read))
        print("\t- content:", response_read)
        print("\t- utf8 content:", str(response_read)[2:-1])


if __name__ == "__main__":
    main()
