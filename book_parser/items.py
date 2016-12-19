# -*- coding: utf-8 -*-
import scrapy


class BookParserItem(scrapy.Item):
    genre = scrapy.Field()
    position = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
    EAN = scrapy.Field()
