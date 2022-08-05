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
    # /html/body/div[3]/div[2]/div[2]/div[3]/div/table/tbody/tr/td[1]/a
    def parse(self, response):
        url = response.url

        settings = get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get(url)
        driver.implicitly_wait(10)
        #/html/body/div[3]/div[2]/div[2]/div[3]/div/table/tbody/tr/td[1]/a
        
        result = dict()
        
        table_rows = Selector(text=driver.page_source).xpath('/html/body/div[3]/div[2]/div[2]/div[3]/div/table/tbody/tr/td').getall()
        for row in table_rows:
            version = Selector(text=row).xpath('.//a/text()').get()
            if version:
                result['Name'] = version.strip()
                yield result

        driver.quit()

                