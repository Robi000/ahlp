#!/usr/bin/python3
"""Module 2-post_email
this will post requst an email adress 
"""
from urllib import parse, request
from sys import argv


def main():
    """
    the programm will run here if __main__
    """
    url = argv[1]
    email = argv[2]
    value = {"email": email}

    data = parse.urlencode(value)
    data = data.encode("utf-8")
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(parse.urldecode(response.read()))


if __name__ == "__main__":
    main()
