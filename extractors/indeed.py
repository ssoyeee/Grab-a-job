from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

import time

posted_date_url = "14"
location_url="United+States"

def get_page_count(keyword):

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) # avoid termination 
    chrome_options.add_argument("--user-agent=Chrome/113.0.5672.6")

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) # create a browser
    #time.sleep(3)
    base_url = "https://www.indeed.com/jobs"

    #browser.get(f"{base_url}?q={keyword}")
    browser.get(f"{base_url}?q={keyword}&fromage={posted_date_url}&l={location_url}")
    wait = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#mosaic-provider-jobcards"))).get_attribute("value")
    print(element)
   
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find('nav', attrs={"aria-label": "pagination"})
    #pagination = soup.find('nav', role='navigation')
    if pagination == None:
        return 1 # amount of page that needs scarping
    # pages = pagination.find_all('div', recursive=False)
    pages = pagination.select('div a')
    # pages = int(count[-1]['aria-label'])+1
    count = len(pages)+1
    for page in pages:
        if page['aria-label']=="Previous Page":
            count -= 1
        if page['aria-label']=="Next Page":
            count -= 1
    if count >= 10:
        return 10
    else:
       return count

    

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True) # avoid termination 
        chrome_options.add_argument("--user-agent=Chrome/113.0.5672.6")

        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) # create a browser
        time.sleep(3)
        base_url = "https://www.indeed.com/jobs"

        #final_url = f"{base_url}?q={keyword}&start={page*10}"
        final_url = f"{base_url}?q={keyword}&fromage={posted_date_url}&l={location_url}&start={page*10}"
        print("Requesting", final_url)
        
        browser.get(final_url)
        time.sleep(5)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        #print(browser.page_source)
        time.sleep(3)
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False) # select only 1 li

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("span", class_="companyLocation")
                job_data = {
                    'link': f"https://www.indeed.com{link}",
                    'company': company.string.replace(","," "),
                    'location': location.string.replace(","," "),
                    'position': title.replace(","," ")
                }
                results.append(job_data)
        print(location)
        # for result in results:
        #     print(result, "\n-----\n")
    return results

