import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.by import By

class AltibaseSpider(scrapy.Spider):
    name = 'altibase'

    start_urls = [
        'http://support.altibase.com/kr/product'
    ]

    def parse(self, response):
        url = response.url

        settings = get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get(url)
        driver.implicitly_wait(3)

        result = dict()
        table_rows = Selector(text=driver.page_source).xpath('//*[@id="productVersion"]/div/table/tbody/tr/td').getall()
        for row in table_rows:
            version = Selector(text=row).xpath('.//a/text()').get()
            if version:
                result['Name'] = Selector(text=row).xpath('.//a/text()').get().strip()
                yield result

        driver.quit()

                