# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RentItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    location_1 = scrapy.Field()
    location_2 = scrapy.Field()
    forward = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()
    pass
