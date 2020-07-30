import scrapy
from ecommerce.items import EcommerceItem

class GmarketBestSpider(scrapy.Spider):
    name = 'gmarket_best'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list > ul > li[id] > a::text').getall()  
        prices = response.css('div.best-list > ul > li[id] > div.item_price > div.s-price > strong > span::text').getall()
                                            # id가 있는 것만 추출 
        # > 바로 밑에 있는 태그 가리킴 (비슷한 태그가 많을 경우에 사용)        
        
        for num, title in enumerate(titles):
            item = EcommerceItem() # 클래스로 객체 생성 
            item['title'] = title # item에 넣어라 
            item['price'] = prices[num].strip().replace("원","").replace(",","") # item에 넣어라 
            yield item # yield 할때마다 items.py의 item 객체에 데이터가 쌓인다.

        
