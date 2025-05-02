import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://quotes.toscrape.com/"

# Send HTTP GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote containers
quotes = soup.find_all("div", class_="quote")

# Loop through each quote block and extract quote text and author
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print(f"{text} — {author}")
