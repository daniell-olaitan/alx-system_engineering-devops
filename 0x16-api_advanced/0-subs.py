#!/usr/bin/python3
"""
function queries a Redit API and returns the number of subscriber
for a given subredit
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Advanced-Api:v1.0 (daniell.olaitan@gmail.com)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
