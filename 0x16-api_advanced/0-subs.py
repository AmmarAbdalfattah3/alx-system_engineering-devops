#!/usr/bin/python3
"""This script queries the Reddit API and returns the number of subscribers
   (not active users, total subscribers) for a given subreddit.
   If an invalid subreddit is given, the function should return 0.
"""


import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-agent/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0


# Example usage:
subreddit = 'python'
print(
    f"Number of subscribers in {subreddit}: {number_of_subscribers(subreddit)}")
