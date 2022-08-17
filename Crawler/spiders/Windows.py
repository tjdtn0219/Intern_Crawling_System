import scrapy
from scrapy.selector import Selector
from Crawler.spiders.test_inherit import SpiderTest


class WindowsSpider(SpiderTest):
    ##윈도우 서버
    name = "windows"
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions',
    ]

#     def parse(self, response):
# #       
#         items = response.xpath('//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr').getall()  #get(), extract() 의 output은 str형태
#         result = dict()
#         for i in range(len(items)):
#             if Selector(text=items[i]).xpath('.//tr/td[1]/a/text()').get():                      #Selector을 이용해서 str 구문 xml로 파싱
#                 result['Version'] = Selector(text=items[i]).xpath('.//tr/td[1]/a/text()').get().strip()       #이어서 할때는 .// 붙이기
#                 date = Selector(text=items[i]).xpath('.//tr/td[2]/text()').get().strip()
#                 if date =="":
#                     date = Selector(text=items[i-1]).xpath('.//tr/td[2]/text()').get().strip()
#                 result['Date'] = date
#                 yield result