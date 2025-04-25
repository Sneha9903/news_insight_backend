import feedparser
import pandas as pd
import os

cities = [
    "Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad",
    "Ahmedabad", "Kolkata", "Pune", "Jaipur", "Lucknow", "Chandigarh",
    "Bhopal", "Indore", "Surat", "Vadodara"
]

def get_news_for_city(city):
    query = f"environment {city}".replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

    print(f"📡 Scraping: {city}")
    try:
        feed = feedparser.parse(url)
        entries = feed.entries[:15]  # limit to top 15
        news_items = []
        for entry in entries:
            news_items.append({
                "City": city,
                "Title": entry.title,
                "URL": entry.link
            })
        return news_items
    except Exception as e:
        print(f"⚠️ Error fetching for {city}: {e}")
        return []

def scrape_all_cities():
    all_news = []
    for city in cities:
        city_news = get_news_for_city(city)
        all_news.extend(city_news)
    return all_news

def save_news_to_csv(news_items):
    df = pd.DataFrame(news_items)
    output_file = os.path.join(os.path.dirname(__file__), "nature_news_india.csv")
    df.to_csv(output_file, index=False)
    print(f"✅ Saved {len(news_items)} articles.")
