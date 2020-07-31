# Crawling_Study
## 크롤링 겁쟁이의 탈쪼랩 성장기 🌱 
<br>

### Xpath 
| File    | Link  | 
| :--------- | --------- | 
| Xpath.ipynb | [Xpath.ipynb](Xpath/Xpath.ipynb)|


```
* 단원별 요약 😊  

Xpath : XML 문서의 특정 요소나 속성에 접근하기 위한 경로를 지정하는 언어

/ : 절대경로
// : 문서내 검색
//@href : href 속성이 있는 모든 태그 선택
//a[@href='http://google.com'] : a태그의 href 속성에 http://google.com 속성값을 가진 모든 태그 선택
(//a)[3] : 문서의 세 번째 링크 선택
(//table)[last()] : 문서의 마지막 테이블 선택
(//a)[position()<3] : 문서의 처음 두 링크 선택
//table/tr/* : 모든 테이블에서 모든 자식 tr 태그 선택
//div[@*] : 속성이 하나라도 있는 div 태그 선택

element_by_xpath : Xpath 사용 함수 

예)  title = driver.find_element_by_xpath('//*[@id="cSub"]/div/h3')
    # 어디에서나 (//) 태그가 cSub인 아이디를 찾아서 ([@id=]) 그 안 div 태그안에 h3 찾은 셈
    print(title.text)

    # 문서 전체에서 title 검색
    title = driver.find_element_by_xpath('//title')
    # head 부분은 get_attribute로 나옴
    print(title.get_attribute('text'))


```
<br>

### Scrapy
| File    | Link  | explanation |
| :--------- | --------- | --------- | 
| python_oop1.ipynb | [oop1.ipynb](Scrapy/python_oop1.ipynb)| 객체지향 프로그래밍 |
| python_oop2.ipynb | [oop2.ipynb](Scrapy/python_oop2.ipynb)| 객체지향 프로그래밍 |
| middlewares(ecommerce).py | [ecommerce.py](/Users/baeyuna/Documents/Crawling/Scrapy/scrapyproject_yuna/ecommerce/ecommerce/spiders/gmarket_best.py)| Scrapy gmarket 크롤러 |
| middlewares(naveropenapi).py | [naveropenapi.py](/Users/baeyuna/Documents/Crawling/Scrapy/crawling_scrapy/scrapyproject/naveropenapi/naveropenapi/middlewares.py)| Scrapy ecommerce 크롤러 |

```
* 단원별 요약 😊  

Scrapy 장점
    1. 크롤링을 안정적으로 할 수 있다.
    2. 크롤링을 좀 더 빠르게 할 수 있다. (멀티 프로세싱)
    3. 다양한 크롤링 관련 기능 (데이터를 다양한 포멧으로 저장 가능)

Scrapy code
    1. scrapy startproject 프로젝트명 
        # 프로젝트 만들겠다.
        # 만들어진 템플릿을 가지고 크롤링을 만든다.
    2. scrapy genspider <크롤러이름> <크롤링페이지주소>
        # 안으로 2번 들어가서, 
        # spider(크롤러) 작성 
        # start_urls 생성 시 자동으로 https:// 가 붙으므로 크롤링페이지주소 작성 시, http:// 안붙이는 게 좋음
        # https://만 지원한다면!! spider 열어서 's' 붙여줘야함.
    3. scrapy crawl 크롤러이름
        # spider(크롤러) 실행 

Scrapy tamplet 
    scrapy.cfg
    프로젝트명/
        __init__.py
        items.py # 어떤 아이템을 가져올건지 선언, 크롤링한 데이터를 item으로 전달해줌 
        pipelines.py 
        settings.py # 
        spiders/
            __init__.py
            크롤러이름.py # 크롤러의 parse함수에서 items.py item에 넣을 데이터 가져옴

scrapy shell
    scrapy shell 주소
    : 해당 주소에서 파싱한 정보 가져와 명령어 하나씩 적용해 정보 볼 수 있음
    : 바로바로 확인할 수 있어, 내가 찾은 선택자가 맞는지 확인 할 때 사용

scrapy response 사용법
    - response.css() : css selector로 데이터 가져오기
        response.scc('head > title').get()    # 하나만 가져오기
        response.scc('head > title').getall() # 리스트 형태로 여러개 가져오기
        response.scc('head > title::text').get()    # 텍스트만 가져오기
        response.css('div.gbest-cate ul.by-group li a::attr("href")').getall() 
                                                    # ::attr("가져오려는 속성값") 

    - response.xpath()
        response.xpath('//div[@class="best-list"]/ul/li/a/text()').getall() 
    
    - 정규표현식 적용 가능
        response.xpath('//div[@class="best-list"]/ul/li/a/text()')[1].re('(\w+)')

scrapy 데이터 저장하기
    scrapy crawl 크롤러명 -o 저장할파일명 -t 저장포멧 
    # json은 한글이 깨짐 -> setting.py에 FEED_EXPORT_ENCODING = 'utf-8' 설정

scrapy pipeline
    - 아이템 데이터 후처리
        - 일부 아이템을 저장하지 않거나,
        - 중복되는 아이템을 저장하지 않거나,
        - 데이터베이스 등에 저장하거나,
        - 특별한 포멧으로 아이템 저장하고 싶거나

    아이템이 저장되려 할 때마다, pipelines.py의 process_item 함수를 호출한다.

```
<br>

### Scrapy_Selenium

여러 페이지 한번에 크롤링하는 spider 만들기

| File    | Link  | explanation |
| :--------- | --------- | --------- | 
| gmarket_category_all | [gmarket_category_all.py](Scrapy_Selenium/scrapy2/scrapy2/spiders/gmarket_category_all.py)| 여러 항복 한번에 크롤링 |


```
* 단원별 요약 😊  

meta
    예) meta={'maincategory_name':category_names[index]})
    # 함수에서 쓰일 값 전달

# 범위를 좁힌 상태로만 가져오기에 뒤이어 css select 사용가능
best_items = response.css('div.best-list') 
    for index, item in enumerate(best_items[1].css('li')):

setting.py
    LOG_FILE = 'log.txt' 
    # 크롤링한 데이터가 너무 많을 경우 터미널 상으로 다 확인하기 어려움 
    # 특정파일에 로그 넣어 데이터를 생성하여 터미널 내용 확인가능

    CONCURRENT_REQUEST = 1
    # 한번에 크롤링 할 수 있는 사이트 1개 -> 하나 크롤링하고 저장 -> 순서대로 랭킹 저자장 (느림....)
    # scrapy는 기본 16개 병렬처리 (=16)

    FEED_EXPORT_FIELDS =[칼럼 리스트 순서대로 삽입]
    # 원하는 순서대로 데이터 넣어서 저장하고 싶다.


```
<br>

### Open API

naver Open API 사용
    openapi.naver.com/v1/search/shop.json?query=


| File    | Link  | explanation |
| :--------- | --------- | --------- | 
|  | [gmarket_category_all.py](Scrapy_Selenium/scrapy2/scrapy2/spiders/gmarket_category_all.py)| 여러 항복 한번에 크롤링 |


```
* 단원별 요약 😊  


```