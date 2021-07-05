# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyFirstScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #排名
    ranking = scrapy.Field()
    #电影名称
    movie_name = scrapy.Field()
    #电影评分
    score = scrapy.Field()
    #评论人数
    score_num = scrapy.Field()
    #格言
    quote = scrapy.Field()
    pass

class DouBanBookItem(scrapy.Item):
    #排名
    ranking = scrapy.Field()
    #书本
    book_name = scrapy.Field()
    #书本评分
    score = scrapy.Field()
    #评论人数
    score_num = scrapy.Field()
    #格言
    quote = scrapy.Field()
    pass
