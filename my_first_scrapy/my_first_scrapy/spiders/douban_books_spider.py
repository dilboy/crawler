import scrapy
from scrapy import Request

from my_first_scrapy.items import MyFirstScrapyItem, DouBanBookItem


class ExampleSpider(scrapy.Spider):
    name = 'doubanBookTop250'
    # allowed_domains = ['example.com']
    # start_urls = ['https://movie.douban.com/top250']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    count = 1
    url = 'https://book.douban.com/top250'

    def start_requests(self):
        yield Request(self.url, headers=self.headers)

    def parse(self, response):
        item = DouBanBookItem()
        books = response.xpath('//*[@id="content"]/div/div[1]/div/table')
        print(books)
        for book in books:
            item["ranking"] = self.count
            self.count += 1
            print(item["ranking"])
            item["book_name"] = book.xpath(
                './/div[@class="pl2"]/a/@title').extract()[0]
            print(item["book_name"])
            item['score'] = book.xpath(
                './/div[@class="star clearfix"]/span[@class="rating_nums"]/text()').extract()[0]
            item['score_num'] = book.xpath(
                './/div[@class="star clearfix"]/span[@class="pl"]/text()').re(r'(\d+)人评价')[0]
            try:
                item['quote'] = book.xpath('.//p[@class="quote"]/span/text()').extract()
            except:
                item['quote'] = ""
            yield item

        next_page_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_page_url:
            next_page_url = next_page_url[0]
            yield Request(next_page_url, headers=self.headers)