import requests
import json
import time

# Function to get Google Autocomplete data
def get_google_autocomplete(keyword):
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={keyword}&gl=bd&hl=en"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        suggestions = json.loads(response.text)[1]
        return suggestions
    else:
        print(f"Failed to retrieve data for {keyword}. Status code: {response.status_code}")
        return []

# Main script
search_query = input('Enter Your Keyword: ')

letters = 'abcdefghijklmnopqrstuvwxyz'

with open(f'{search_query}.txt', 'a') as file:
    for letter in letters:
        query = f"{search_query} {letter}"
        suggestions = get_google_autocomplete(query)

        for suggestion in suggestions:
            file.write(suggestion.strip() + '\n')
            print(suggestion.strip())

        # Sleep to avoid overwhelming the server
        time.sleep(1)  # Delay to avoid hitting rate limits
