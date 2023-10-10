#!/usr/bin/python3
"""Function that queries the Reddit API and returns no. of subbies"""
import requests


def number_of_subscribers(subreddit):
    """Method returns the total no. of subbies on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "advance_API_tut/1.0 (by /u/Worried-Ad3891)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    no_subbies = response.json().get("data")
    return no_subbies.get("subscribers")
