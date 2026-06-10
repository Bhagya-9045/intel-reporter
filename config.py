from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

COMPANIES = [
    "Razorpay",
    "PhonePe",
    "Zepto",
    "Groww",
    "CRED"
]

MAX_ARTICLES_PER_COMPANY = 10