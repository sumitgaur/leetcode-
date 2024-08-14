# Given
# there
# are
# 2
# functions:
#
# Webpage
# LoadWebpage(const
# URL & url);
# void
# ParseUrls(const
# Webpage & page, std::vector < URL > & urls);
# Generate site map within same domain
# wikipedia.com  -> india () within wikipedia
# implement site map generator
# input -> an url
# output ->   p0 -> p1,p2,p3
#             p1-> p3,p4
#             p3->p0
import random
from collections import defaultdict


# pages = P
# edges = E
# O(P + E) dfs

class WebPage:
    def __init__(self):
        self.id = random.Random()

    def __eq__(self, other):
        pass


class SiteMapGenerator:
    def __init__(self, seed_url):
        self.seed_url = seed_url
        self.site_map = defaultdict(list)  # adjacency list   url -> ref links webpage->webpages

    def load_web_page(self, urls):
        """
        # load page in memory  need to return only urls, free the memory
        Return the webpage 3 way handshaking, web socket TCP/IP of wikipedia, connection Pools
        daemon thread to keep on downloading
        :param url:
        :return:
        """
        # load in parallel joining the thread future
        pass

    def parse_urls(self, web_page):
        """
        Return all the urls for same domain
        :return:
        """
        pass

    def generate_site_map(self): # taking too much time
        """
        1. heap dump
        2. Depth pruning threshold to stop the depth d
        3. I/O operations
        :return:
        """
        visited_pages = set()

        def _dfs(url):
            if url not in visited_pages:  # O(1)
                visited_pages.add(url)
                web_page = self.load_web_page(url)
                next_urls = self.parse_urls(web_page)
                self.site_map[url] = next_urls
                for next_url in next_urls:
                    self._dfs(next_url)

        _dfs(self.seed_url)
        return self.site_map

    # def generate_site_map(self, in_url): # another API
    #     if in_url not in self.site_map:
    #         self.generate_site_map()
    #     return self.site_map
