# report_generator.py
# This file's job: Take AI analysis results and create a beautiful HTML report

import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def generate_html_report(all_results):
    """
    Takes analysis results and creates a beautiful HTML file.
    Think of this like: taking your notes and designing a magazine page.
    """

    # Get today's date for the report title
    today = datetime.now().strftime("%B %d, %Y")

    # Start building the HTML page
    # This is like writing the skeleton of a webpage
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Competitive Intelligence Report - {today}</title>
    <style>
        /* CSS = styling, like choosing fonts and colors */
        body {{
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }}
        .company-card {{
            background: white;
            border-radius: 10px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .company-name {{
            font-size: 24px;
            font-weight: bold;
            color: #1a1a2e;
            margin-bottom: 15px;
        }}
        .sentiment-positive {{ color: #27ae60; font-weight: bold; }}
        .sentiment-negative {{ color: #e74c3c; font-weight: bold; }}
        .sentiment-neutral  {{ color: #f39c12; font-weight: bold; }}
        .trend-growing   {{ color: #27ae60; }}
        .trend-declining {{ color: #e74c3c; }}
        .trend-stable    {{ color: #f39c12; }}
        .analysis-text {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #1a1a2e;
            white-space: pre-wrap;
            font-size: 14px;
            line-height: 1.6;
        }}
        .meta {{
            color: #888;
            font-size: 13px;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔍 Competitive Intelligence Report</h1>
        <p>Generated on {today} | Indian Fintech Tracker</p>
        <p>{len(all_results)} companies analyzed</p>
    </div>
"""

    # Loop through each company and add a card for it
    for company, result in all_results.items():

        analysis = result["analysis"]
        article_count = result["article_count"]

        # Figure out CSS class for color coding
        if "Positive" in analysis:
            sentiment_class = "sentiment-positive"
            sentiment_emoji = "📈"
        elif "Negative" in analysis:
            sentiment_class = "sentiment-negative"
            sentiment_emoji = "📉"
        else:
            sentiment_class = "sentiment-neutral"
            sentiment_emoji = "➡️"

        if "Growing" in analysis:
            trend_class = "trend-growing"
            trend_emoji = "🚀"
        elif "Declining" in analysis:
            trend_class = "trend-declining"
            trend_emoji = "⬇️"
        else:
            trend_class = "trend-stable"
            trend_emoji = "➡️"

        # Add this company's card to the HTML
        html += f"""
    <div class="company-card">
        <div class="company-name">{sentiment_emoji} {company}</div>
        <div class="meta">Articles analyzed: {article_count} | Report date: {today}</div>
        <div class="analysis-text">{analysis}</div>
    </div>
"""

    # Close the HTML page
    html += """
</body>
</html>
"""

    return html


def save_report(html_content):
    """
    Saves the HTML report to the reports/ folder.
    """

    # Create filename with today's date
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"intel_report_{now}.html"

    # Full path to save the file
    reports_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
    filepath = os.path.join(reports_dir, filename)

    # Write HTML to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Report saved: {filepath}")
    return filepath


if __name__ == "__main__":

    # Import the analyzer to get fresh results
    from agents.analyzer import analyze_all_companies

    print("Running AI analysis...")
    results = analyze_all_companies()

    print("\nGenerating HTML report...")
    html = generate_html_report(results)

    filepath = save_report(html)

    print(f"\nDone! Open this file in your browser:")
    print(f"{filepath}")
    print("\nTip: Right-click the file in VS Code → 'Reveal in Explorer' → double-click to open!")