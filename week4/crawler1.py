
class CrawlerASite:
    url = "https://www.google.com"

    def crawl(self):
        print(f"{self.url} do crawl")

cas = CrawlerASite()
cas.crawl()