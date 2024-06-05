#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles of
   all hot articles for a given subreddit. If no results are found for
   the given subreddit, the function should return None.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-agent/0.1'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None


# Example usage:
subreddit = 'python'
titles = recurse(subreddit)
if titles:
    for title in titles:
        print(title)
else:
    print(None)
