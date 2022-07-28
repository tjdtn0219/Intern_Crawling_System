import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from selenium import webdriver

class JBOSS_Spider(scrapy.Spider):
    name = 'jboss'

    start_urls = [
        'https://developers.redhat.com/products/eap/download',
    ]

    def parse(self, response):
        url = response.url

        settings = get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get(url)
        # driver.implicitly_wait(3)

        iframe_source = driver.page_source

        items = scrapy.Selector(text=iframe_source).xpath('//*[@id="assembly-field-downloads-page-content-29465"]/div/div').getall()

        # print(items)
        result = dict()

        for item in items:
            version = Selector(text=item).xpath('.//h3/text()').get()
            date = Selector(text=item).xpath('.//div[1]/div[3]/span/text()').get()
            if "EAP" not in version:
                result['Name'] = version
                result['Date'] = date
                yield result
            
        driver.quit()
