#!/usr/bin/python3
"""
Module contains a function that queries an API and returns a
list of all hot posts for a given Reddit subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """function queries an API and returns a list of all
    hot posts for a given Reddit subreddit

    Args:
        subreddit (str): The given user
        hot_list (list): list of hot posts for the given user
        after (str): used for API pagination to fetch the next slice of data
        count (int): the current length of hot_list

    Returns: a list of all the hot posts for the given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'Ubuntu:Advanced-Api:v1.0'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
