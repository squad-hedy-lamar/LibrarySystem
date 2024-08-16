#importar Copy 
#importar Genre
#importar Author
from typing import List, Optional

class Book:
# title, Publisher, genres, authors, copies = private
# max_renewals = public
# add_copy(str), borrow_copy, return_copy

    def __init__(self, title: str, publisher: str, genres: List[Genre], authors: List[Author], max_renewals: int):
        self.__title = title
        self.__publisher = publisher
        self.__genres = genres
        self.__authors = authors
        self.__copies = []
        self.max_renewals = max_renewals
    #
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        self.__title = value
    #
    
    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        self.__publisher = value
    #
    
    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, value):
        self.__genres = value
    #
    
    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        self.__authors = value
    #
    
    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, value):
        self.__copies = value
    #
