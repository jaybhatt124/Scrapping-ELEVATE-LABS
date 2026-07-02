"""
Web Scraper for News Headlines
Fetches top headlines from BBC News and saves them to a .txt file.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.bbc.com/news"
OUTPUT_FILE = "headlines.txt"

# A User-Agent header helps avoid being blocked by some sites
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


def fetch_html(url):
    """Fetch the raw HTML of the page."""
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()  # raises an error for bad status codes (404, 500, etc.)
    return response.text


def extract_headlines(html):
    """Parse the HTML and pull out headline text from <h2> tags."""
    soup = BeautifulSoup(html, "html.parser")

    headlines = []
    for h2 in soup.find_all("h2"):
        text = h2.get_text(strip=True)
        if text and len(text) > 10:  # skip empty/junk short tags
            headlines.append(text)

    # Remove duplicates while keeping order
    seen = set()
    unique_headlines = []
    for h in headlines:
        if h not in seen:
            seen.add(h)
            unique_headlines.append(h)

    return unique_headlines


def save_headlines(headlines, filename):
    """Write headlines to a text file with a timestamp."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Top Headlines - Scraped on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        for i, headline in enumerate(headlines, start=1):
            f.write(f"{i}. {headline}\n")


def main():
    print(f"Fetching headlines from {URL} ...")
    try:
        html = fetch_html(URL)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

    headlines = extract_headlines(html)

    if not headlines:
        print("No headlines found. The site's HTML structure may have changed.")
        return

    save_headlines(headlines, OUTPUT_FILE)
    print(f"Found {len(headlines)} headlines. Saved to '{OUTPUT_FILE}'.\n")

    print("Preview:")
    for h in headlines[:5]:
        print(f"- {h}")


if __name__ == "__main__":
    main()