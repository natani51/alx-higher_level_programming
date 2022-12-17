import urllib.request

# Fetch the URL
url = "https://alx-intranet.hbtn.io/status"

# Use a with statement to open the URL
with urllib.request.urlopen(url) as response:
    # Read and decode the response
    html = response.read().decode()

    # Split the response into lines
    lines = html.split("\n")

    # Print each line preceded by a "-"
    for line in lines:
        print("-", line)
