import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

# ─────────────────────────────────────────
# WEB SCRAPER — by Faizal Khan
# Scrapes job listings from a website
# and saves the data into a CSV file.
# ─────────────────────────────────────────

# We scrape "Books to Scrape" — a free legal
# practice website made for learning scraping.
BASE_URL = "http://books.toscrape.com/catalogue/"
START_URL = "http://books.toscrape.com/"


def get_page(url):
    """
    Downloads a webpage and returns
    a BeautifulSoup object to parse it.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the HTML content
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"❌ Failed to fetch: {url} (Status: {response.status_code})")
        return None


def scrape_books(max_pages=3):
    """
    Scrapes book titles, prices, ratings,
    and availability from multiple pages.
    """
    all_books = []
    url = START_URL
    page_num = 1

    rating_map = {
        'One': 1, 'Two': 2, 'Three': 3,
        'Four': 4, 'Five': 5
    }

    print(f"\n🔍 Scraping up to {max_pages} pages...\n")

    while url and page_num <= max_pages:
        print(f"📄 Scraping page {page_num}...")
        soup = get_page(url)

        if not soup:
            break

        # Find all book containers on the page
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            # Extract title
            title = book.h3.a['title']

            # Extract price
            price = book.find('p', class_='price_color').text.strip()
            # Remove the pound symbol and convert to float
            price_clean = float(price.replace('£', '').replace('Â', ''))

            # Extract star rating (stored as a word in the class)
            rating_word = book.find('p', class_='star-rating')['class'][1]
            rating = rating_map.get(rating_word, 0)

            # Extract availability
            availability = book.find('p', class_='instock availability').text.strip()

            all_books.append({
                'Title': title,
                'Price (£)': price_clean,
                'Rating (out of 5)': rating,
                'Availability': availability
            })

        # Find the "next" page button
        next_btn = soup.find('li', class_='next')
        if next_btn:
            next_page = next_btn.a['href']
            # Handle relative URLs
            if 'catalogue/' in next_page:
                url = BASE_URL + next_page
            else:
                url = BASE_URL + next_page
            page_num += 1
        else:
            break

    return all_books


def save_to_csv(books, filename=None):
    """
    Saves the list of books to a CSV file.
    """
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"books_data_{timestamp}.csv"

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Title', 'Price (£)', 'Rating (out of 5)', 'Availability'])
        writer.writeheader()
        writer.writerows(books)

    print(f"\n✅ Data saved to: {filename}")
    return filename


# ─── MAIN PROGRAM ───
if __name__ == "__main__":
    print("=" * 50)
    print("       🌐 Python Web Scraper")
    print("       Scraping: books.toscrape.com")
    print("=" * 50)

    try:
        pages = int(input("\nHow many pages to scrape? (1-50): ").strip())
        pages = max(1, min(pages, 50))
    except ValueError:
        pages = 3

    books = scrape_books(max_pages=pages)

    if books:
        print(f"\n📚 Total books scraped: {len(books)}")
        save_to_csv(books)

        # Show a preview of first 5
        print("\n📋 Preview (first 5 results):")
        print("-" * 60)
        for book in books[:5]:
            print(f"  {book['Title'][:45]:<45} £{book['Price (£)']:.2f}  ⭐{book['Rating (out of 5)']}")
    else:
        print("❌ No data scraped.")
