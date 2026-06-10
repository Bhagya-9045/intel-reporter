import requests
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import NEWS_API_KEY, COMPANIES, MAX_ARTICLES_PER_COMPANY
from agents.database import create_database, save_articles

def fetch_news_for_company(company_name):
    url = "https://newsapi.org/v2/everything"
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    params = {
        "q": company_name,
        "from": week_ago,
        "sortBy": "relevancy",
        "language": "en",
        "pageSize": MAX_ARTICLES_PER_COMPANY,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data["status"] == "ok":
        return data["articles"]
    else:
        print(f"Error for {company_name}: {data['message']}")
        return []

def collect_all_company_news():
    all_news = {}
    for company in COMPANIES:
        print(f"Fetching news for: {company}...")
        articles = fetch_news_for_company(company)
        all_news[company] = articles
        print(f"  Found {len(articles)} articles")
    return all_news

if __name__ == "__main__":
    print("=" * 50)
    print("STARTING NEWS COLLECTION + SAVING TO DATABASE")
    print("=" * 50)

    create_database()
    news_data = collect_all_company_news()

    print("\nSaving to database...")
    total_saved = 0

    for company, articles in news_data.items():
        saved = save_articles(company, articles)
        total_saved += saved
        print(f"  Saved {saved} new articles for {company}")

    print(f"\nDone! Total new articles saved: {total_saved}")