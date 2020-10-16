import scrapy
import datetime

class QuotesSpider(scrapy.Spider):
    name = "News"
    # start_urls = ["https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101"]
    def start_requests(self):
        urls = [
            "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
