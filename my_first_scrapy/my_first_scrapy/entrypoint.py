from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', 'doubanTop250', '-o douban.csv'])
execute(['scrapy', 'crawl', 'doubanBookTop250', '-o douban_book.csv'])