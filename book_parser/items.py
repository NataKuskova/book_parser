# -*- coding: utf-8 -*-
import scrapy


class BookParserItem(scrapy.Item):
    position = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
