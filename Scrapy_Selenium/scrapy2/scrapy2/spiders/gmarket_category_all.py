import scrapy
from scrapy2.items import Scrapy2Item

class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'

    # start_requests있으면 이 함수 먼저 실행한다!
    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback=self.parse_mainpages)
        # 저 주소를 크롤링하고, callback의 함수를 호출하라

    # response가 꼭 있어야 주소에서 크롤링한 정보가 넘어갈 수 있다.
    def parse_mainpages(self, response):
        print("parse_mainpages")
        category_links = response.css('div.gbest-cate ul.by-group li a::attr(href)').getall()
        category_names = response.css('div.gbest-cate ul.by-group li a::text').getall()

        # 1st category crawling
        for index, category_link in enumerate(category_links):
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link, callback=self.parse_items, meta={'main_category_name':category_names[index], 'sub_category_name': 'ALL' })
        # 2nd category crawling
        for index, category_link in enumerate(category_links):
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link, callback=self.parse_subcategory, meta={'main_category_name':category_names[index] })


    def parse_subcategory(self, response):
        print ("parse_subcategory", response.meta['main_category_name'])
        subcategory_links = response.css('div.navi.group > ul > li > a::attr(href)').getall()
        sub_category_names = response.css('div.navi.group > ul > li > a::text').getall()
        for index, subcategory_link in enumerate(subcategory_links):
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + subcategory_link, callback=self.parse_items, meta={'main_category_name':response.meta['main_category_name'], 'sub_category_name':sub_category_names[index] })


    def parse_items(self, response):
        print ("parse_maincategory", response.meta['main_category_name'], response.meta['sub_category_name'])

        best_items = response.css('div.best-list') # 범위를 좁힌 상태로만 가져오기에 뒤이어 css select 사용가능
        for index, item in enumerate(best_items[1].css('li')):
            doc = Scrapy2Item() # 저장할 아이템 객체 생성
            ranking = index + 1
            title = item.css('a.itemname::text').get()
            ori_price = item.css('div.o-price::text').get() 
            dis_price = item.css('div.s-price strong span span::text').get()
            discount_percent = item.css('div.s-price em::text').get()

            if ori_price == None:
                ori_price = dis_price
            ori_price = ori_price.replace("원","").replace(",","")
            dis_price = dis_price.replace("원","").replace(",","")
            if discount_percent == None:
                discount_percent = 0
            else:
                discount_percent = discount_percent.replace('%',"")

            # 저장할 아이템 설정
            doc['main_category_name'] = response.meta['main_category_name']
            doc['sub_category_name'] = response.meta['sub_category_name']
            doc['ranking'] = ranking
            doc['title'] = title
            doc['ori_price'] = ori_price
            doc['dis_price'] = dis_price
            doc['discount_percent'] = discount_percent

            # print(ranking, title, ori_price, dis_price, discount_percent)
            yield doc
