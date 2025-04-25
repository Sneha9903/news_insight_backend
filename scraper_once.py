# backend/scrape_once.py
from scraper import scrape_all_cities, save_news_to_csv

if __name__ == "__main__":
    print("📅 Running scheduled news scrape on Render...")
    news = scrape_all_cities()
    save_news_to_csv(news)
    print("✅ Scraping done.")
