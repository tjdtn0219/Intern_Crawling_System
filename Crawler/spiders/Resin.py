import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from selenium import webdriver

class ResinSpider(scrapy.Spider):
    name = 'resin'

    start_urls = [
        'https://caucho.com/resin-4.0/changes/release-notes.xtp',
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

        items = scrapy.Selector(text=iframe_source).xpath('/html/body/table[2]/tbody/tr/td[3]/h2/a/text()').getall()

        result = dict()
        for item in items:
            result['Version'] = item
            yield result
        driver.quit()
