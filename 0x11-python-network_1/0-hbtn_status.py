#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status
import urllib.request
import urllib.error

try:
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        req = response.read()
        print("Body response:\n\t- type: {}"
              "\n\t- content: {}\n\t- utf8 content: {}"
              .format(type(req), req, req.decode('utf-8')))
except urllib.error.URLError as e:
    print(e)
