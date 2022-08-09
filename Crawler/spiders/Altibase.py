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
        driver.implicitly_wait(20)
        
        element = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[3]/div/table/tbody/tr")

        table_rows = Selector(text = element.get_attribute('innerHTML')).xpath('.//td/a/text()').getall()

        result = dict()

        for row in table_rows:
            result['Version'] = row.strip()
            yield result

        driver.quit()

                