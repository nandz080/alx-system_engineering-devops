#!/usr/bin/python3
"""Function that queries the Reddit API and  prints hot posts on a given subreddit"""
import requests


def top_ten(subreddit):
    """Method prints titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "advance_API_tut/1.0 (by /u/Worried-Ad3891)"
    }
    limit = {"limit": 10}
    response = requests.get(url, headers=headers, params=limit,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    posts = response.json().get("data")
    [print(post.get("data").get("title")) for post in posts.get("children")]
