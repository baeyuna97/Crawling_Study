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
| File    | Link  | 
| :--------- | --------- | 
