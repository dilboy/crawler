from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'doubanTop250', '-o douban.csv'])