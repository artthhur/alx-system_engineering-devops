#!/usr/bin/python3
"""
Module 100-count.py that contains the function count_words
"""
import re
import requests


def count_words(subreddit, word_list, dict_count={}, after=None):
    """
    recursive function that queries the Reddit API, parses the
    title of all hot articles, and prints a sorted count of
    given keywords
    """
    if subreddit is None:
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "0x16-api_advanced:project:v1.0.0"}
    params = {"after": after}

    r = requests.get(url, params=params, headers=user_agent)

    if r.status_code == 200:
        data = r.json().get("data")
        after = data.get("after")
        if not after:
            dict_count = sorted(dict_count.items(),
                                key=lambda x: (-x[1], x[0]))
            for word, count in dict_count:
                print('{}: {}'.format(word, count))
            return
        for post in data.get("children"):
            for word in word_list:
                word = word.lower()
                pattern = re.escape(word)
                title = post.get('data').get('title').lower()
                count = len(re.findall(r'\b{}\b'.format(pattern), title))
                if count > 0:
                    dict_count[word] = dict_count.get(word, 0) + count
        return count_words(subreddit, word_list, dict_count, after)
