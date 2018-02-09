# -*- coding: utf-8 -*-
import scrapy


class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['https://www.reddit.com']
    start_urls = ['http://https://www.reddit.com/']

    def parse(self, response):
        pass
