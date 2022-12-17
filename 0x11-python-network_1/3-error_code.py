#!/usr/bin/python3
""" HTTPError Handling python script
"""

from sys import argv
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
