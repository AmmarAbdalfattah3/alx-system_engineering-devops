#!/usr/bin/python3
"""This script queries the Reddit API and prints the titles of
   the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'custom-agent/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)


# Example usage:
subreddit = 'python'
top_ten(subreddit)
