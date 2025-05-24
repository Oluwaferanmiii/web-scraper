import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://quotes.toscrape.com/page/"

page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    page_url = url+str(page)
    # Send HTTP GET request
    response = requests.get(page_url)

    # Check to see if we're on the last page
    if "No quotes found!" in response.text:
        break

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quote containers
    quotes = soup.find_all("div", class_="quote")

    # Loop through each quote block and extract quote text and author
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        print(f"{text} — {author}")

    page += 1
