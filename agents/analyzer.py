# analyzer.py
# Same as before but using Groq (free) instead of Claude API

from groq import Groq       # Groq is our free AI provider
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import GROQ_API_KEY, COMPANIES
from agents.database import get_articles_for_company


def analyze_company(company_name):
    # Get articles from database
    articles = get_articles_for_company(company_name)

    if not articles:
        print(f"No articles found for {company_name}")
        return None

    # Convert articles to text
    articles_text = ""
    for i, article in enumerate(articles[:10]):
        title = article[1]
        source = article[2]
        description = article[5]
        articles_text += f"\nArticle {i+1}:\n"
        articles_text += f"Title: {title}\n"
        articles_text += f"Source: {source}\n"
        articles_text += f"Description: {description}\n"
        articles_text += "-" * 30

    # Instructions for AI
    prompt = f"""
You are a competitive intelligence analyst.
Analyze these recent news articles about {company_name} and provide:

1. SENTIMENT: Overall sentiment (Positive/Negative/Neutral) with a score from 1-10
2. KEY SIGNALS: Top 3 important business signals or events detected
3. TREND: Is the company growing, declining, or stable?
4. SUMMARY: One paragraph summary of what's happening with this company

Here are the articles:
{articles_text}

Respond in this exact format:
SENTIMENT: [Positive/Negative/Neutral] (Score: X/10)
KEY SIGNALS:
- Signal 1
- Signal 2
- Signal 3
TREND: [Growing/Declining/Stable]
SUMMARY: [Your paragraph here]
"""

    # Connect to Groq (free AI)
    client = Groq(api_key=GROQ_API_KEY)

    # Send to AI and get response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",    # updated free model 
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    # Extract the text from response
    response_text = response.choices[0].message.content

    return {
        "company": company_name,
        "analysis": response_text,
        "article_count": len(articles)
    }


def analyze_all_companies():
    print("=" * 50)
    print("STARTING AI ANALYSIS")
    print("=" * 50)
    all_results = {}
    for company in COMPANIES:
        print(f"\nAnalyzing {company}...")
        result = analyze_company(company)
        if result:
            all_results[company] = result
            print(f"  Analysis complete for {company}")
    return all_results


if __name__ == "__main__":
    results = analyze_all_companies()
    print("\n" + "=" * 50)
    print("AI ANALYSIS RESULTS")
    print("=" * 50)
    for company, result in results.items():
        print(f"\n{'='*40}")
        print(f"COMPANY: {company}")
        print(f"Articles analyzed: {result['article_count']}")
        print(f"\n{result['analysis']}")