# News Headline Scraper

A Python script that scrapes top headlines from BBC News and saves them to a text file.

## Features
- Fetches live HTML using `requests`
- Parses `<h2>` headline tags using `BeautifulSoup`
- Removes duplicate/junk entries
- Saves results to `headlines.txt` with a timestamp

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`

Install dependencies:
```bash
pip install requests beautifulsoup4
```

## How to Run
```bash
python scraper.py
```

## Output
Creates `headlines.txt` in the same folder, formatted like:
```
Top Headlines - Scraped on 2026-07-02 15:27:09
============================================================

1. Headline one...
2. Headline two...
```

## Files
| File | Description |
|------|--------------|
| `scraper.py` | Main scraper script |
| `headlines.txt` | Auto-generated output file (created on run) |

## Notes
- Targets `https://www.bbc.com/news` by default — change the `URL` variable in `scraper.py` to scrape a different site.
- News sites update their HTML structure periodically. If you get 0 headlines, inspect the page's `<h2>` tags in your browser and adjust the `soup.find_all()` selector (e.g. add a class filter) accordingly.