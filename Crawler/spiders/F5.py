import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.by import By

class F5Spider(scrapy.Spider):
    name = 'f5'

    start_urls = [
        'https://support.f5.com/csp/article/K33062581'
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

        driver.find_element(By.XPATH,'//*[@id="articleContainer"]/div[2]/div/div[2]/div/div/table/tbody')
        result = dict()
        table_rows = Selector(text=driver.page_source).xpath('.//tr').getall()

        # print(element.get_attribute('innerHTML')) << element를 받으면 이렇게 반환

        for row in table_rows:
            if Selector(text=row).xpath('.//td[1]/strong/text()').get():
                result['Name'] = Selector(text=row).xpath('.//td[1]/strong/text()').get().strip()
                result['Date'] = Selector(text=row).xpath('.//td[4]/strong/text()').get().strip()
                yield result
        driver.quit()
                