# -*- coding: utf-8 -*-
import scrapy
from disney_spider.items import DisneySpiderItem


class DisneyWaitTimeSpider(scrapy.Spider):
    """
    Parses the Disneyland/Disney Sea attraction wait time page and extracts
    the following data:

        * park name
        * attraction name
        * attraction id (taken from attraction link url)
        * wait time
        * last updated datetime
        * attraction status
    """

    name = "disney_wait_time_spider"

    start_urls = [
            "http://info.tokyodisneyresort.jp/rt/s/gps/tdl_index.html?nextUrl=http://info.tokyodisneyresort.jp/rt/s/realtime/tdl_attraction.html&lat=35.6274489&lng=139.8840183",
            "http://info.tokyodisneyresort.jp/rt/s/gps/tds_index.html?nextUrl=http://info.tokyodisneyresort.jp/rt/s/realtime/tds_attraction.html&lat=35.6274489&lng=139.8840183",
            ]

    def parse(self, response):
        for sel in response.xpath('//li[@class="midArw"]'):
            item = DisneySpiderItem()
            item['land_name'] = sel.xpath('../../p[not(@class)]/text()').extract()
            item['attraction_name'] = sel.xpath('a/div[@class="about"]/h3/text()').extract()
            item['attraction_id'] = map(lambda x: x[x.rfind(':')+1:-1], sel.xpath('a/@href').extract())
            item['wait_time'] = sel.xpath('a/div[@class="time"]/p[@class="waitTime"]/strong/text()').extract()
            item['updated'] = sel.xpath('a/p[@class="update"]/text()').extract()
            item['status'] = sel.xpath('a/div[@class="about"]/p[@class="run"]/text()[string-length() > 2]').extract()
            yield item
