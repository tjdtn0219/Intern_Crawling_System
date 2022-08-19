import scrapy
from scrapy.utils.project import get_project_settings
from selenium import webdriver
import re

class AlteonSpider(scrapy.Spider):
    name = 'alteon'
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['ALTEON']
    ]

    def parse(self, response):
        url = response.url + "#page/APSoluteVision_4.30_RN%2FAPSoluteVision_4.30_RN.1.12.html%23"

        driver_path = AlteonSpider.settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get(url)
        # driver.implicitly_wait(3)
        driver.switch_to.frame("page_iframe")

        iframe_source = driver.page_source

        # items = scrapy.Selector(text=r).xpath('//html/body/div/div/div[1]/div[3]/table/tbody/tr/td[1]/div/text()').getall()
        items = scrapy.Selector(text=iframe_source).xpath('//*[@id="page_content"]/div[3]/table/tbody//tr/td[1]/div/text()').getall()

        result = dict()

        for item in items:
            version_value = re.sub(r'[^0-9.x]', '', str(item))
            if version_value:
                result['Version'] = item
                yield result

        driver.quit()
