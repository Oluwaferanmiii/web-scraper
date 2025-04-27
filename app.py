import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Step 2: Check if request was successful
if response.status_code == 200:
    # Step 3: Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 4: Print the raw HTML (just to see it works)
    print(soup.prettify())
else:
    print("Failed to retrieve the page")
