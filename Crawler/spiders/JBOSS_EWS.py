import scrapy
from scrapy.selector import Selector

class JBOSS_EWS_Spider(scrapy.Spider):
    name = "jbossews"
    start_urls = [
        'https://access.redhat.com/documentation/en-us/red_hat_jboss_web_server/5.6',
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="cp-content"]/div[2]/div/div/div[1]/div[2]/div/ul/li').getall()

        result = dict()

        for item in items:
            version = Selector(text=item).xpath('.//label/text()').get()
            result['Name'] = version.strip()
            yield result        
            #/html/body/table[2]/tbody/tr/td[3]/h2[1]/a