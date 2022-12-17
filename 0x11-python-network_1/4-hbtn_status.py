#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """


import requests


if __name__ == '__main__':
    res = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
