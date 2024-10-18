import streamlit as st
import requests
import json
import time

# Function to get Google Autocomplete data
def get_google_autocomplete(keyword):
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={keyword}&gl=us&hl=en"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        suggestions = json.loads(response.text)[1]
        return suggestions
    else:
        st.error(f"Failed to retrieve data for {keyword}. Status code: {response.status_code}")
        return []

# Streamlit interface
st.title("Google Autocomplete Suggestions")
search_query = st.text_input("Enter Your Keyword:")

if st.button('Get Suggestions'):
    if search_query:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        all_suggestions = []
        
        with st.spinner('Fetching suggestions...'):
            for letter in letters:
                query = f"{search_query} {letter}"
                suggestions = get_google_autocomplete(query)
                
                if suggestions:
                    all_suggestions.extend(suggestions)
                # Sleep to avoid overwhelming the server
                time.sleep(1)

        if all_suggestions:
            st.success(f"Suggestions for '{search_query}':")
            for suggestion in all_suggestions:
                st.write(suggestion)
            
            # Option to download suggestions as a text file
            suggestions_str = "\n".join(all_suggestions)
            st.download_button(
                label="Download Suggestions as Text",
                data=suggestions_str,
                file_name=f"{search_query}_suggestions.txt",
                mime="text/plain"
            )
        else:
            st.warning("No suggestions found.")
    else:
        st.warning("Please enter a keyword to search.")
