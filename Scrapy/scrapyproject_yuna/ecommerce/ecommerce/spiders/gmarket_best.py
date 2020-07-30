import scrapy
from ecommerce.items import EcommerceItem

class GmarketBestSpider(scrapy.Spider):
    name = 'gmarket_best'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.xpath('//div[@class="best-list"]/ul/li/a/text()').getall()  
        prices = response.css('div.best-list ul li div.item_price div.s-price strong span::text').getall()
        # prices = response.xpath('//div[@class="best-list"]/ul/li/div[@class="item_price"]/div[@class="s-price"]/strong/span/text()').getall()  
        
        for num, title in enumerate(titles):
            item = EcommerceItem() # 클래스로 객체 생성 
            item['title'] = title # item에 넣어라 
            item['price'] = prices[num] # item에 넣어라 
            yield item # yield 할때마다 items.py의 item 객체에 데이터가 쌓인다.

        
