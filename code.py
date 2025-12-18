import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"

# 1. Get the main page
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# 2. Find all books
books = soup.find_all("article", class_="product_pod")

# 3. Extract book links (absolute URLs)
book_urls = [urljoin(base_url, book.find("h3").find("a")["href"]) for book in books]

# 4. Parse the first book page
book_page = requests.get(book_urls[0])
book_soup = BeautifulSoup(book_page.text, "html.parser")
title = book_soup.find("h1").text
price = book_soup.find("p", class_="price_color").text
availability = book_soup.find("p", class_="instock availability").text.strip()
print("Title:", title)
print("Price:", price)
print("Availability:", availability)
