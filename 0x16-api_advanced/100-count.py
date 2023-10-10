#!/usr/bin/python3
"""Function that queries the Reddit API,  parses the title of all hot articles, and prints a sorted count"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """Prints counts of given words found in hot posts of a given subreddit"""
    if counts is None:
        counts = {}

    # Base case: if no words in the list, print the counts
    if not word_list:
        print_counts(counts)
        return

    # Reddit API URL for getting hot posts in a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    # If there's an 'after' parameter, add it to the URL to get the next page of results
    if after:
        url += f'&after={after}'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'advance_API_tut (by /u/Worried-Ad3891)'}

    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and count the occurrences of words in titles
        for post in data['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                word_lower = word.lower()
                if word_lower in title:
                    counts[word_lower] = counts.get(word_lower, 0) + 1

        # Check if there are more pages to retrieve
        if data['data']['after'] is not None:
            # Recursively call the function with the 'after' parameter
            count_words(subreddit, word_list, after=data['data']['after'], counts=counts)
        else:
            # If no more pages, print the final counts
            print_counts(counts)
    elif response.status_code == 404:
        # If subreddit not found, print nothing
        return
    else:
        # Print an error message for other cases
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")

def print_counts(counts):
    # Sort the counts in descending order by count and then alphabetically by word
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the sorted counts
    for word, count in sorted_counts:
        print(f"{word}: {count}")

# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit_name = sys.argv[1]
        keywords = sys.argv[2].split()
        count_words(subreddit_name, keywords)

