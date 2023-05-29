from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# for replit
chrome_options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("detach", True) # avoid termination 

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) # create a browser

browser.get("https://www.indeed.com/jobs?q=python&limit=50")
print(browser.page_source)

browser.get("https://www.naver.com")
