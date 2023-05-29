from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # avoid termination 

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) # create a browser

base_url = "https://www.indeed.com/jobs"
search_term = "python"

browser.get(f"{base_url}?q={search_term}")
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive=False)
print(len(jobs))

for job in jobs:
    print(job)
    print("-----------")
    print("-----------")
