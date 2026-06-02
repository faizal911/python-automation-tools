# 🌐 Python Web Scraper

Scrapes book data (title, price, rating, availability) from [books.toscrape.com](http://books.toscrape.com) and saves it to a CSV file.

## 📌 What it does
- Scrapes multiple pages automatically
- Extracts: Title, Price, Star Rating, Availability
- Saves clean data to a timestamped CSV file
- Shows a preview of results in the terminal

## 🛠️ Requirements

```bash
pip install requests beautifulsoup4
```

## ▶️ How to run

```bash
python scraper.py
```

Then enter how many pages to scrape (each page has 20 books).

## 📂 Output example

```
📚 Total books scraped: 60

📋 Preview (first 5 results):
────────────────────────────────────────────────────────────
  A Light in the Attic                      £51.77  ⭐3
  Tipping the Velvet                        £53.74  ⭐1
  Soumission                                £50.10  ⭐1
  Sharp Objects                             £47.82  ⭐4
  Sapiens: A Brief History                  £54.23  ⭐5

✅ Data saved to: books_data_20260602_104500.csv
```

## 🔧 Customisation
You can adapt this scraper for any website by changing the CSS selectors in `scrape_books()`.

## 👨‍💻 Author
**Faizal Khan** — Python Developer & Automation Specialist  
[Fiverr](https://www.fiverr.com/faizalpathan369) | [GitHub](https://github.com/faizal911)
