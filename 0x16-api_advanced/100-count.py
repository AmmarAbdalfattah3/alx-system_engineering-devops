#!/usr/bin/python3
"""This script queries the Reddit API, parses the title of all
   hot articles, and prints a sorted count of given keywords
   (case-insensitive, delimited by spaces. Javascript should
   count as javascript, but java should not).
"""


import requests
from collections import Counter
import re


def count_words(subreddit, word_list, hot_list=[], after=None):
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
                return count_words(subreddit, word_list, hot_list, after)
            else:
                return process_words(hot_list, word_list)
        else:
            return None
    except requests.RequestException:
        return None


def process_words(hot_list, word_list):
    word_counter = Counter()
    word_set = set(word.lower() for word in word_list)
    word_pattern = re.compile(
        r'\b(' +
        '|'.join(
            re.escape(word) for word in word_set) +
        r')\b',
        re.IGNORECASE)

    for title in hot_list:
        words_found = word_pattern.findall(title)
        word_counter.update(word.lower() for word in words_found)

    sorted_words = sorted(word_counter.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_words:
        print(f"{word}: {count}")


# Example usage:
subreddit = 'python'
keywords = ['python', 'java', 'javascript', 'html', 'css']
count_words(subreddit, keywords)
