# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbItem(scrapy.Item):
    data = scrapy.Field() # json data of the airbnb API listing

    def __repr__(self):
        return f"AirbnbListing[{self['data']['listing']['id']}]"
