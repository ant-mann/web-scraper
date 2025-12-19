Nature Journal Web Scraper

A robust Python-based web scraper designed to crawl multiple pages of the Nature.com article archive. This tool automates the process of identifying specific article types (e.g., "Research Highlight," "News"), extracting their content, and organizing them into a structured local directory.
🚀 Features

    Multi-Page Crawling: Dynamically navigates through a user-specified number of result pages.

    Article Filtering: Filters articles by category (type) based on user input.

    Automated Directory Management: Creates organized Page_N folders for each page processed.

    Content Extraction: Parses full article bodies and saves them as .txt files with cleaned, filesystem-friendly filenames.

🛠️ Tech Stack

    Python 3

    Requests: To handle HTTP GET requests and navigate the web.

    BeautifulSoup4: To parse HTML and extract specific data attributes and body text.

    OS & String Modules: For directory creation and filename sanitization.

📂 Project Structure

When the script runs, it generates a directory structure like this:
Plaintext

.
├── scraper.py          # Main application logic
├── Page_1/             # Articles found on page 1
│   ├── Article_Title_One.txt
│   └── Article_Title_Two.txt
├── Page_2/             # Articles found on page 2 (even if empty)
└── ...

⚙️ How It Works

    User Input: The script prompts for the number of pages to scrape and the specific type of article to save.

    URL Construction: It iterates through the Nature archive using query parameters (?page=N).

    Parsing: For every page, it identifies all <article> tags and checks the data-test='article.type' attribute.

    File I/O: If a match is found, the script follows the article link, extracts the body text from the c-article-body or article__teaser classes, and writes it to a file.

📝 Usage

    Clone the repository.

    Ensure you have the required libraries installed:
    Bash

pip install requests beautifulsoup4

Run the script:
Bash

python scraper.py

Enter your parameters when prompted:
Plaintext

    > 4
    > Nature Briefing
    Saved all articles.

🎓 Context

This project was developed as part of the JetBrains Academy "Web Scraper" track. It focuses on mastering HTTP status codes, handling dynamic URL parameters, and managing local file systems in Python.
