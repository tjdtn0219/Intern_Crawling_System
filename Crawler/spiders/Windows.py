import scrapy
from scrapy.selector import Selector

class WindowsSpider(scrapy.Spider):
    ##윈도우 서버
    name = "windows"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions',
    ]

    def parse(self, response):
#       
        items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr').getall()  #get(), extract() 의 output은 str형태
        result = dict()
        for item in items:
            if Selector(text=item).xpath('.//tr/td[1]/a/text()').get():                      #Selector을 이용해서 str 구문 xml로 파싱
                result['Version'] = Selector(text=item).xpath('.//tr/td[1]/a/text()').get().strip()       #이어서 할때는 .// 붙이기
                result['Date'] = Selector(text=item).xpath('.//tr/td[2]/text()').get().strip()
                yield result