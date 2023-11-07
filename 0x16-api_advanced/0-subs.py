#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "my_script:reddit_api:v1.0.0 (by /u/Nickname-Pending1)"
    }
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    result = resp.json().get("data")
    return result.get("subscribers")
