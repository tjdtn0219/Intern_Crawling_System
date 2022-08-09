import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from selenium import webdriver

class JuniperSpider(scrapy.Spider):
    name = 'juniper'

    start_urls = [
        'https://support.juniper.net/support/eol/software/junos/'
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

        page_source = driver.page_source
 
        #/html/body/sw-page/main/sw-eol-table/div/table/tbody/tr
        table_rows = scrapy.Selector(text=page_source).xpath('/html/body/sw-page/main/sw-eol-table/div/table/tbody/tr').getall()

        result = dict()
        for row in table_rows:
            result['Version'] = Selector(text=row).xpath('.//td[1]/text()').get().strip()
            result['Date'] = Selector(text=row).xpath('.//td[2]/text()').get().strip()
            yield result

        driver.quit()