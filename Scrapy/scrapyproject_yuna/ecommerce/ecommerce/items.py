# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcommerceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # extract할 데이터 선언
    title = scrapy.Field()
    price = scrapy.Field()
