#!/usr/bin/env python3

class Book:
    def __init__(self, title=None, page_count=None):
        self._title = None
        self._page_count = None
        if title is not None and page_count is not None:
            self.title = title
            self.page_count = page_count
        else:
            raise ValueError("title and page_count are required")
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

        

    
        