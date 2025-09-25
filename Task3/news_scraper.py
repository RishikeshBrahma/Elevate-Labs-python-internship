
from bs4 import BeautifulSoup

import requests

# URL of a news website (example: BBC)
URL = "https://www.bbc.com/news"

def fetch_headlines(url):
    # Send HTTP request
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch the webpage. Status code:", response.status_code)
        return []

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find headline tags (adjust based on site structure)
    headlines = []
    for h in soup.find_all(['h2', 'h3']):  
        text = h.get_text(strip=True)
        if text:  # Avoid empty strings
            headlines.append(text)

    return headlines

def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for line in headlines:
            f.write(line + "\n")
    print(f"✅ Saved {len(headlines)} headlines to {filename}")

if __name__ == "__main__":
    headlines = fetch_headlines(URL)
    if headlines:
        save_to_file(headlines)
    else:
        print("No headlines found.")
