import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

class JBOSS_EWS_Spider(scrapy.Spider):
    name = "jbossews"
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['JBOSS_EWS']
    ]

    def parse(self, response):
        items = response.xpath('//*[@id="cp-content"]/div[2]/div/div/div[1]/div[2]/div/ul/li').getall()

        result = dict()

        for item in items:
            version = Selector(text=item).xpath('.//label/text()').get()
            result['Version'] = version.strip()
            result['Date'] = None
            yield result        
            #/html/body/table[2]/tbody/tr/td[3]/h2[1]/a