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
| middlewares(ecommerce).py | [ecommerce.py](/Users/baeyuna/Documents/Crawling/Scrapy/crawling_scrapy/scrapyproject/ecommerce/ecommerce/middlewares.py)| Scrapy ecommerce 크롤러 |
| middlewares(naveropenapi).py | [naveropenapi.py](/Users/baeyuna/Documents/Crawling/Scrapy/crawling_scrapy/scrapyproject/naveropenapi/naveropenapi/middlewares.py)| Scrapy ecommerce 크롤러 |

```
* 단원별 요약 😊
Scrapy 프레임워크  
    - 함수와 코드를 미리 작성해놨다.
    - 특정 함수를 특정 위치에 어떻게 사용해야 하는지, 작성해야 하는지를 정해놓은 프로그램
    - 직접 구현할 필요없다 !! 

Scrapy 장점
    1. 크롤링을 안정적으로 할 수 있다.
    2. 크롤링을 좀 더 빠르게 할 수 있다. (멀티 프로세싱)
    3. 다양한 크롤링 관련 기능 (데이터를 다양한 포멧으로 저장 가능)

사용방법
    - 실제 크롤링할 스파이더(spider, scrapy 기반 크롤러 프로그램) 생성
    - 크롤링할 사이트, 아이템에 대한 selector 설정
    - 크롤러 실행 

Scrapy code
    1. scrapy startproject 프로젝트명 
        # 프로젝트 만들겠다.
        # 만들어진 템플릿을 가지고 크롤링을 만든다.
    2. scrapy genspider <크롤러이름> <크롤링페이지주소>
        # spider(크롤러) 작성 
    3. scrapy crawl 크롤러이름
        # spider(크롤러) 실행

Scrapy tamplet
    scrapy.cfg
    ecommerce/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
```


