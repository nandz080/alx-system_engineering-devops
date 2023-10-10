#!/usr/bin/python3
"""Function that queries Reddit API and returns a list of all hot posts on a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Method returns a list of titles of all hot articls on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "advance_API_tut (by /u/Worried-Ad3891)"
    }
    variables = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=variables,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    articles = response.json().get("data")
    after = articles.get("after")
    count += articles.get("dist")
    for hot_articles in articles.get("children"):
        hot_list.append(hot_articles.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
