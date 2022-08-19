import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

class ExtremeSpider(scrapy.Spider):
    name = 'extreme'
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['EXTREME']
    ]
#//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[1]
    def parse(self, response):
        url = response.url

        driver_path = ExtremeSpider.settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get(url)
        driver.implicitly_wait(10)

        result = dict()
        table_rows = Selector(text=driver.page_source).xpath('//*[@id="DataTables_Table_0"]/tbody/tr').getall()

        for row in table_rows:
            if Selector(text=row).xpath('.//td[1]/text()').get():
                #result['Date'] = Selector(text=row).xpath('.//td[1]/text()').get().strip()
                name = Selector(text=row).xpath('.//td[2]/a/text()').get().strip()
                result['Version'] = name.replace("Release Notes", "").strip()
                result['Date'] = Selector(text=row).xpath('.//td[3]/text()').get().strip()
                yield result

        driver.quit()

                