import requests
from pages.quote_pages import Quote

page_content = requests.get("http://quotes.toscrape.com/").content

page = Quote(page_content)

for quote in page.Data:
    print(quote)
