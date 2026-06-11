🔍 Intel Reporter — AI-Powered Competitive Intelligence
Show Image Show Image Show Image Show Image

🤖 Intel Reporter is a full-stack AI application that automatically tracks Indian fintech startups, analyzes news sentiment using Llama 3 AI, and generates weekly competitive intelligence reports — completely FREE!

🚀 Live Demo: Click here to view the app

🎯 What Problem Does This Solve?
A human analyst spends 5-6 hours daily reading news, tracking competitors, and writing reports. This is expensive and slow.
Intel Reporter does it automatically in seconds.

✨ Key Features
📊 Core Features

📰 Auto News Collection — Fetches latest news for 5 Indian fintech companies daily
🤖 AI Analysis — Llama 3 reads articles and extracts smart business insights
📊 Sentiment Scoring — Scores each company Positive / Negative / Neutral out of 10
📈 Trend Detection — Detects if company is Growing / Declining / Stable
📄 Report Generation — Auto-generates beautiful HTML reports every week
🖥️ Live Dashboard — Interactive Streamlit website to explore all data

🏢 Companies Being Tracked
CompanySector💳 RazorpayPayment Gateway📱 PhonePeDigital Payments🛒 ZeptoQuick Commerce📈 GrowwInvestment Platform💰 CREDFintech Rewards

🧰 Tech Stack
LayerTechnologyLanguagePython 3.11Data CollectionNewsAPI + Python RequestsDatabaseSQLite built into PythonAI EngineGroq API + Llama 3 70BDashboardStreamlitDeploymentStreamlit Cloud FreeVersion ControlGitHub

🗂️ Project Structure
intel-reporter/
│
├── agents/
│   ├── news_collector.py    # Fetches news from NewsAPI
│   ├── analyzer.py          # AI analysis using Groq + Llama 3
│   └── database.py          # SQLite database operations
│
├── reports/
│   └── report_generator.py  # Generates beautiful HTML reports
│
├── dashboard/
│   └── app.py               # Streamlit live dashboard
│
├── data/
│   └── articles.db          # SQLite database file
│
├── config.py                # Central settings and API keys
├── requirements.txt         # All Python dependencies
└── .env                     # Secret API keys (not uploaded to GitHub)

🚀 Installation and Setup
1. Clone the Repository
git clone https://github.com/Bhagya-9045/intel-reporter.git
cd intel-reporter
2. Create Virtual Environment
Windows:
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Set Up Environment Variables
Get your free API keys from:

👉 NewsAPI key from https://newsapi.org
👉 Groq API key from https://console.groq.com

Create a .env file in root folder and add:
NEWS_API_KEY=your_newsapi_key_here
GROQ_API_KEY=your_groq_key_here
Note: The .env file is ignored by Git to keep your keys secure.
5. Run the Application
# Step 1 - Collect news articles
python agents/news_collector.py

# Step 2 - Run AI analysis
python agents/analyzer.py

# Step 3 - Generate HTML report
python reports/report_generator.py

# Step 4 - Launch live dashboard
streamlit run dashboard/app.py
Open your browser and go to http://localhost:8501 🎉

📊 Sample AI Output
COMPANY: Groww
─────────────────────────────────────────
SENTIMENT: Positive (Score: 8/10)

KEY SIGNALS:
- Goldman Sachs bought significant stake in Groww parent company
- Net profit surged 122 percent year on year
- Mutual fund arm adopting multicap strategy for better returns

TREND: Growing 🚀

SUMMARY: Groww is on a strong growth trajectory with major
institutional investment and record profits this quarter.
The company continues to expand its financial services offerings.

🆓 Total Cost = ₹0
ToolFree TierNewsAPI100 requests per dayGroq AIGenerous free tierSQLiteCompletely freeStreamlit CloudFree hostingGitHubFree repositories
I built this entire project without spending a single rupee!

🎓 What I Learned Building This
I started this project as a complete beginner with basic Python knowledge. By the end I learned:

✅ REST API integration with Python
✅ Database design and queries with SQLite
✅ AI and LLM prompt engineering
✅ Data pipeline architecture
✅ Web dashboard development with Streamlit
✅ Free cloud deployment on Streamlit Cloud
✅ Git and GitHub version control
✅ Securing API keys and secrets

This project gave me hands on experience with skills used daily at companies like Swiggy, Razorpay, and Groww.

🔮 Future Plans

🐦 Add Twitter and Reddit sentiment tracking
💼 Add LinkedIn job posting tracker to detect aggressive hiring
📧 Send weekly email reports automatically
🏢 Track more Indian startups across different sectors
📉 Add stock price and funding round data
⏰ Schedule automatic weekly runs


🤝 Contributing
Contributions are welcome! Here is how you can help:

Fork the project
Create your feature branch git checkout -b feature/AmazingFeature
Commit your changes git commit -m 'Add some AmazingFeature'
Push to the branch git push origin feature/AmazingFeature
Open a Pull Request


👋 About Me and Contact
Bhagyashree
Fresher Python Developer and AI Enthusiast
📍 Bangalore, Karnataka, India
For any questions or feedback, feel free to reach out:
📧 shreesajjan9045@gmail.com
