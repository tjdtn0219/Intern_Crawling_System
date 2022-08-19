# Scrapy settings for Crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Crawler'

SPIDER_MODULES = ['Crawler.spiders']
NEWSPIDER_MODULE = 'Crawler.spiders'
CHROME_DRIVER_PATH = '/var/lib/jenkins/Projects/LSSWARE_Crawler/chromedriver'

VERSION_HEADS = ["version", "name", "release", "series", "general availability"]
DATE_HEADS = ["first release", "release date", "date of issue", "latest release"]
LIST_FORMATS = [
        "%B %d, %Y", "%d %B %Y", "%Y-%m-%d", "%B %Y", "%Y/%m/%d", "%b %Y", "%d/%m/%Y",
        "%m/%d/%Y", "%Y.%m", "%B\u00a0%d, %Y", "%d\u00a0%B %Y", "%Y"
    ]

URLS = {
    'AIX' : 'https://en.wikipedia.org/wiki/IBM_AIX',
    'ALTEON' : 'https://portals.radware.com/releasenotes/APSolute_Vision_Release_Notes_4_30/',
    'ALTIBASE' : 'http://support.altibase.com/kr/product',
    'APACHE' : 'https://en.wikipedia.org/wiki/Apache_HTTP_Server',
    'AVAYA' : 'https://www.devconnectprogram.com/site/global/products_resources/avaya_aura_communication_manager/releases/10_1/index.gsp',
    'CENTOS' : 'https://en.wikipedia.org/wiki/CentOS',
    'CISCO' : 'https://www.cisco.com/c/ko_kr/support/ios-nx-os-software/index.html#allDevices',
    'CRITIX' : 'https://www.citrix.com/downloads/citrix-adc/firmware/',
    'CUBRID' : 'https://en.wikipedia.org/wiki/CUBRID',
    'DB2' : 'https://en.wikipedia.org/wiki/IBM_Db2',
    'EXTREME' : 'https://www.extremenetworks.com/support/release-notes/product/extremexos-software/',
    'F5' : 'https://support.f5.com/csp/article/K33062581',
    'HP_UX' : 'https://en.wikipedia.org/wiki/HP-UX',
    'IIS' : 'https://docs.microsoft.com/en-us/lifecycle/products/internet-information-services-iis',
    'INFORMIX' : 'https://www.cursor-distribution.de/en/ibm-software/support-informix/informix-lifecycle-tab-en',
    'IPLANET' : 'https://en.wikipedia.org/wiki/Oracle_iPlanet_Web_Server',
    'JBOSS_EWS' : 'https://access.redhat.com/documentation/en-us/red_hat_jboss_web_server/5.6',
    'JBOSS' : 'https://developers.redhat.com/products/eap/download',
    'JEUS' : 'https://en.wikipedia.org/wiki/JEUS',
    'JUNIPER' : 'https://support.juniper.net/support/eol/software/junos/',
    'MARIADB' : 'https://en.wikipedia.org/wiki/MariaDB',
    'MSSQL' : 'https://en.wikipedia.org/wiki/History_of_Microsoft_SQL_Server#SQL_Server_2017',
    'MYSQL' : 'https://en.wikipedia.org/wiki/MySQL',
    'NGINX' : 'http://nginx.org/en/download.html',
    'OHS' : 'https://www.oracle.com/kr/middleware/technologies/webtier-downloads.html',
    'ORACLEDB' : 'https://en.wikipedia.org/wiki/Oracle_Database',
    'ORACLELINUX' : 'https://en.wikipedia.org/wiki/Oracle_Linux',
    'POSTGRES_SQL' : 'https://en.wikipedia.org/wiki/PostgreSQL',
    'PROLINUX' : 'https://technet.tmaxsoft.com/ko/front/download/findDownloadList.do?cmProductCode=0702',
    'REDHAT' : 'https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux',
    'RESIN' : 'https://caucho.com/resin-4.0/changes/release-notes.xtp',
    'SOLARIS' : 'https://en.wikipedia.org/wiki/Oracle_Solaris',
    'SUSE' : 'https://en.wikipedia.org/wiki/SUSE_Linux',
    'SYBASE' : 'https://infocenter.sybase.com/help/index.jsp?noscript=1',
    'SYBASEIQ' : 'https://infocenter.sybase.com/help/index.jsp?noscript=1',
    'TIBERO' : 'https://technet.tmaxsoft.com/ko/front/download/findDownloadList.do?cmProductCode=0301',
    'TOMCAT' : 'https://en.wikipedia.org/wiki/Apache_Tomcat',
    'WEBLOGIC' : 'https://en.wikipedia.org/wiki/Oracle_WebLogic_Server',
    'WEBSPHERE' : 'https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server',
    'WEBTOB' : 'https://technet.tmaxsoft.com/ko/front/download/findDownloadList.do?cmProductCode=0102',
    'WINDOWS' : 'https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions',

}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Crawler.middlewares.CrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Crawler.middlewares.CrawlerDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Crawler.pipelines.CrawlerPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
