# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DisneySpiderItem(scrapy.Item):
    land_name = scrapy.Field()
    attraction_name = scrapy.Field()
    attraction_id = scrapy.Field()
    wait_time = scrapy.Field()
    updated = scrapy.Field()
    status = scrapy.Field()

