# Auto Crawler System

## Purpose
- Scrape OS releases data from web-sites, and detect and send a mail if new release version is update.

## System Flow Diagram
<img src="https://github.com/tjdtn0219/LSSWARE_Crawler/assets/76704436/0f6f9599-478e-46e5-8495-1e81997d3747">

## Jenkins Pipeline Details
<img src="https://github.com/tjdtn0219/LSSWARE_Crawler/assets/76704436/420d85f4-4a67-4c4e-963f-4e57eab12634">



## Enviroment Setting

- You need to make virtual Environment and set it in the venv

- Python & pip3 Version
    + Python 3.10.3 , pip 22.0.2
    <pre><code>$ sudo apt-get install python3-scrapy python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
    </code></pre>

- Scrapy Version
    + Scrapy 2.5.1
    <pre><code>$ pip3 install scrapy </code></pre>

- ChromeDriver
    <pre><code>$ sudo apt-get update</code></pre>
    <pre><code>$ sudo apt-get upgrade</code></pre>
    <pre><code>$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb</code></pre>
    <pre><code>$ sudo apt install ./google-chrome-stable_current_amd64.deb </code></pre>
    <pre><code>$ google-chrome --version</code></pre>
    <pre><code>$ wget [google-chrome 버전과일치하는 chromedriver 버전.zip 링크] </code></pre>
    <pre><code>$ unzip chromedriver_linux64.zip </code></pre>
    <pre><code>$ cd chromedriver [shell_scripts/]
    
    *If you want to change location of chromedriver, move it and modify [CHROME_DRIVER_PATH] in settings.py</code></pre>


- Selenium
    <pre><code>$ pip3 install scrapy</code></pre>

