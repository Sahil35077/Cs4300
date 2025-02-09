import requests

def fetch_google():
    """Fetches Google homepage and returns the status code."""
    response = requests.get("https://www.google.com")
    return response.status_code