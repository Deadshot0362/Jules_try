import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    """
    Extracts the text content from a given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
