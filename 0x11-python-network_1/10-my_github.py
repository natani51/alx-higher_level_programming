#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    print(requests.get(
        "https://api.github.com/user",
        auth=HTTPBasicAuth(sys.argv[1], sys.argv[2])).json().get("id"))
