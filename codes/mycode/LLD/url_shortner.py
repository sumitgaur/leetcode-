'''
Design and implement a URL Shortener Service that converts long URLs into short, unique URLs and redirects users to the original URL when the short URL is accessed.

https://www.google.com/search?body=.///////
https://bit.py/asdasda

FR
- system should provide an API to shorten the URL
- system should redirect shorten url to original url
- each shorten url should be unique
- system shuld extend to allow custom alias (optional)
- system should expire shorten url, if url is expired return appropriate error message

NFR
- service should be thread safe
- system should ensure idempotency for the repeated requests
'''
import abc
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

"https://www.goog.com?search-sadasd" -> "https://www.bit.py/", TTL


# controller -> service -> repository -> storage (inmemory/db/,,,)
@dataclass
class URLMapping:
    short_key: str
    long_url: str
    created_timestamp: datetime
    expiry: datetime
    is_active: bool


class URLShortenerException(Exception):
    pass


class InvalidURLException(URLShortenerException):
    pass


class UrlExpiredException(URLShortenerException):
    pass


class URLRepository(ABC):
    @abstractmethod
    def save(self, ):
        pass

    @abstractmethod
    def find(self):
        pass


class InMemoryURLRepository(URLRepository):

    def save(self):
        pass

    def find(self):
        pass


# strategy
class KeyGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class URLService(ABC):
    @abstractmethod
    def shorten(self):
        pass


class URLServiceImpl(URLService):
    def shorten(self):
        pass


class URLController:
    def shorten(self):
        pass

    def redirect(self):
        pass

if __name__ == '__main__':
    # URLController -> URLServiceImpl(gives strategy and repo)
    #                 ->URLRepository saves


