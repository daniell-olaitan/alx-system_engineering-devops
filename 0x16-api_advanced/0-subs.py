#!/usr/bin/python3
"""
function that queries the Reddit API and return the number of
subcribers for a given subredit
"""
import requests


def number_of_subscribers(subreddit):
    """function queries the Reddit API and return the number of
    subcribers for a given subredit
    Args:
        subreddit (str): a given user

    Return: the number of given subscribers for the given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Ubuntu:Advanced-Api:v1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
