from bs4 import BeautifulSoup

from locators.quotes_page_locators import PageQuotes
from parsers.quotes import QuotesParser


class Quote:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser").content

    def Data(self):
        locators = PageQuotes.QUOTE
        quotes_tags = self.soup.select(locators)
        return [QuotesParser(e) for e in quotes_tags]

