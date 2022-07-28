import scrapy
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from selenium import webdriver

class SybaseSpider(scrapy.Spider):
    name = "sybase"
    start_urls = [
        'https://infocenter.sybase.com/help/index.jsp?noscript=1',
    ]

#/html/body/table/tbody/tr[3]
    def parse(self, response):
        url = response.url

        settings = get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        driver.get(url)
        driver.implicitly_wait(3)
        driver.switch_to.frame("HelpFrame")
        driver.switch_to.frame("ViewsFrame")
        driver.switch_to.frame("tocViewFrame")

        frame_source = driver.page_source
        items = scrapy.Selector(text=frame_source).xpath('/html/body/table/tbody/tr').getall()
        result = dict()
        for item in items:
            version = scrapy.Selector(text=item).xpath('.//td/b/a/text()').get().strip()
            if "Japanese" in version and "Adaptive Server Enterprise" in version:
                result['Name'] = version
                yield result

        driver.quit()