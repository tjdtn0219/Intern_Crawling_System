import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from Crawler.Funcs import Funcs

class F5Spider(scrapy.Spider):
    name = 'f5'
    settings = get_project_settings()
    start_urls = [
        settings['URLS']['F5']
    ]

    def parse(self, response):
        url = response.url

        driver_path = F5Spider.settings['CHROME_DRIVER_PATH']
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
                result['Version'] = Selector(text=row).xpath('.//td[1]/strong/text()').get().strip()
                result['Date'] = Funcs.date_to_str(Selector(text=row).xpath('.//td[4]/strong/text()').get().strip())
                yield result
        driver.quit()
                