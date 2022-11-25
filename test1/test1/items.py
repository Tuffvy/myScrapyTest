# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    location = scrapy.Field()
    houseType = scrapy.Field()
    area = scrapy.Field()
    unitPrice = scrapy.Field()
    totalPrice = scrapy.Field()
    pass


class SecondItem(scrapy.Item):
    name = scrapy.Field()
    location = scrapy.Field()
    houseType = scrapy.Field()
    area = scrapy.Field()
    unitPrice = scrapy.Field()
    totalPrice = scrapy.Field()
    pass
