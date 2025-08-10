"""
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to fetch web pages. 
These tasks are I/O-bound because they spend a lot of time waiting for responses from servers.
Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.
"""

import threading
import requests
import bs4

urls = [
    "https://python.langchain.com/v0.2/docs/introduction/",
    "https://python.langchain.com/v0.2/docs/concepts/",
    "https://python.langchain.com/v0.2/docs/tutorials/"
]

def fetch_page(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")


def main(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_page, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    print("All pages fetched successfully.")

if __name__ == "__main__":
    main(urls)
