# database.py
# This file's job: Create our database and save/read articles from it

# sqlite3 is built into Python — no installation needed!
import sqlite3

# os lets us work with file paths
import os

# This is where our database file will be saved
# It will create a file called articles.db inside the data/ folder
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "articles.db")


def create_database():
    """
    Creates the database and table if they don't exist yet.
    Think of this like: creating a new Excel file with column headers.
    """

    # connect() opens the database file (creates it if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)

    # cursor is like a pen — we use it to write commands to the database
    cursor = conn.cursor()

    # CREATE TABLE IF NOT EXISTS = "make this table only if it's not already there"
    # This prevents errors if we run the script twice
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            title TEXT,
            source TEXT,
            url TEXT,
            published_at TEXT,
            description TEXT,
            collected_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Save the changes to the file
    conn.commit()

    # Close the connection (like closing the Excel file)
    conn.close()

    print(f"Database ready at: {DB_PATH}")


def save_articles(company_name, articles):
    """
    Saves a list of articles for one company into the database.
    Think of this like: pasting rows into your Excel sheet.
    """

    # Open the database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Count how many articles we actually saved
    saved_count = 0

    # Loop through each article
    for article in articles:

        # Check if this article URL already exists in database
        # This prevents saving the same article twice
        cursor.execute("SELECT id FROM articles WHERE url = ?", (article.get("url"),))
        exists = cursor.fetchone()  # Returns None if not found

        # Only save if article doesn't already exist
        if not exists:
            cursor.execute("""
                INSERT INTO articles (company, title, source, url, published_at, description)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                company_name,                           # company name
                article.get("title", ""),               # article title
                article.get("source", {}).get("name", ""),  # source name
                article.get("url", ""),                 # article URL
                article.get("publishedAt", ""),         # publish date
                article.get("description", "")          # short description
            ))
            saved_count += 1

    # Save all changes
    conn.commit()
    conn.close()

    return saved_count


def get_articles_for_company(company_name):
    """
    Reads articles for one company FROM the database.
    Think of this like: filtering your Excel sheet by company name.
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # SELECT = "fetch these columns"
    # WHERE = "only rows where company matches"
    # ORDER BY = "newest articles first"
    cursor.execute("""
        SELECT company, title, source, url, published_at, description
        FROM articles
        WHERE company = ?
        ORDER BY published_at DESC
    """, (company_name,))

    # fetchall() gets ALL matching rows as a list
    rows = cursor.fetchall()
    conn.close()

    return rows


def get_total_article_count():
    """
    Returns total number of articles saved in database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM articles")
    count = cursor.fetchone()[0]  # Get the number from the result
    conn.close()
    return count