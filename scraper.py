import requests
import string
import os
from bs4 import BeautifulSoup

# Take parameters from user input
num_pages = int(input())
type_of_article = input()

base_url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"

for page_num in range(1, num_pages + 1):
    # Create directory for the current page
    dir_name = f"Page_{page_num}"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    # Construct page-specific URL
    url = f"{base_url}&page={page_num}"
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')

        for article in articles:
            article_type_span = article.find('span', attrs={'data-test': 'article.type'})
            link_tag = article.find('a', attrs={'data-track-action': 'view article'})

            # Filter by the user-provided article type
            if article_type_span and article_type_span.text.strip() == type_of_article and link_tag:
                title = link_tag.text.strip()
                clean_title = title.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_')
                filename = os.path.join(dir_name, f"{clean_title}.txt")

                # Get full article content
                article_url = "https://www.nature.com" + link_tag.get('href')
                article_response = requests.get(article_url)
                article_soup = BeautifulSoup(article_response.content, 'html.parser')

                # Identify article body
                body_div = article_soup.find('div', attrs={'class': 'c-article-body'})
                if not body_div:
                    body_div = article_soup.find('p', attrs={'class': 'article__teaser'})
                
                content = body_div.text.strip() if body_div else ""

                # Save the file into the respective Page_N folder
                with open(filename, 'wb') as f:
                    f.write(content.encode('utf-8'))

print("Saved all articles.")