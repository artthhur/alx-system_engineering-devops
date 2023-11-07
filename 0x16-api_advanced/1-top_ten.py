#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "my_script:reddit_api:v1.0.0 (by /u/Nickname-Pending1)"
    }
    params = {
        "limit": 10
    }
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if resp.status_code == 404:
        print("None")
        return
    result = resp.json().get("data")
    [print(c.get("data").get("title")) for c in result.get("children")]
