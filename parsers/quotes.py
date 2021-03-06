from locators.quotes_locators import Quotes


class QuotesParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"This article {self.Content} by {self.Author}"
    @property
    def Content(self):
        locator = Quotes.CONTENT
        return self.parent.select_one(locator).string
    @property
    def Author(self):
        locator = Quotes.AUTHOR
        return self.parent.select_one(locator).string
    @property
    def tags(self):
        locator = Quotes.TAGS
        return [e.string for e in self.parent.select_one(locator)]
