# Nature Journal Web Scraper

A multi-page web scraping application built with Python that extracts articles from the [Nature.com](https://www.nature.com) archive. The program automates the process of navigating search results, filtering by article category, and saving content into a structured local directory.

## 🚀 Features

* **Dynamic Multi-Page Crawling**: Scrapes a user-defined number of result pages by manipulating URL parameters.
* **Selective Extraction**: Filters articles based on specific types (e.g., "Research Highlight", "News", "Nature Briefing") provided via user input.
* **Automated Data Organization**: Automatically creates and manages nested directories (`Page_1`, `Page_2`, etc.) for clean data storage.
* **Filename Sanitization**: Processes article titles by removing punctuation and replacing spaces with underscores to ensure filesystem compatibility.
* **Robust Parsing**: Utilizes `BeautifulSoup4` to navigate complex HTML structures and extract the core article body.

## 🛠️ Technical Stack

* **Python 3.x**
* **Requests**: For handling HTTP protocols and managing session headers.
* **BeautifulSoup4**: For DOM traversal and data extraction.
* **OS Library**: For directory management and file I/O operations.

## 📂 Directory Structure

Upon execution, the script organizes extracted data as follows:
```
.
├── scraper.py          # Main application logic
├── Page_1/             # Articles found on page 1
│   ├── Article_Title_One.txt
│   └── Article_Title_Two.txt
├── Page_2/             # Articles found on page 2 (even if empty)
└── ...
```

## ⚙️ How to Run

### Prerequisites

Ensure you have Python installed, then install the necessary dependencies:
```
pip install requests beautifulsoup4
```

### Execution

1. Run the script from your terminal:
`python scraper.py`
2. Provide the requested inputs:
    * **Number of pages**: The total number of pages to crawl (e.g., `5`).
    * **Article type**: The exact string of the category to filter (e.g., `Research Highlight`).

### Example
```
2
News
Saved all articles.
```

## 🎓 Learning Objectives

This project was completed as part of the **JetBrains Academy** Python Developer track. Key concepts practiced include:

* Processing HTTP response status codes.
* Working with the `BeautifulSoup` library for web parsing.
* Managing file systems and binary file writing in Python.
* Implementing control flow for iterative scraping across multiple web endpoints.
