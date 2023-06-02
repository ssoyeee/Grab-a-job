from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

posted_date_url = "14"
exclude_url="-clearance"
location_url="United+States"

def get_page_count(keyword):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) # avoid termination 
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) # create a browser

    base_url = "https://www.indeed.com/jobs"
    posted_date_url = "14"
    exclude_url="-clearance"
    location_url="United+States"

    #browser.get(f"{base_url}?q={keyword}")
    browser.get(f"{base_url}?q={keyword}+{exclude_url}&fromage={posted_date_url}&l={location_url}")
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find('nav', attrs={"aria-label": "pagination"})
    #pagination = soup.find('nav', role='navigation')
    if pagination == None:
        return 1 # amount of page that needs scarping
    pages = pagination.find_all('div', recursive=False)
    #count = pagination.select('div a')
    # pages = int(count[-1]['aria-label'])+1
    count = len(pages)
    if count >= 5:
        return 5
    else:
       return count

    

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True) # avoid termination 

        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) # create a browser
    
        base_url = "https://www.indeed.com/jobs"

        #final_url = f"{base_url}?q={keyword}&start={page*10}"
        final_url = f"{base_url}?q={keyword}+-{exclude_url}&fromage={posted_date_url}&l={location_url}&start={page*10}"
        print("Requesting", final_url)
        
        browser.get(final_url)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False) # select only 1 li

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link': f"https://www.indeed.com{link}",
                    'company': company.string,
                    'location': location.string,
                    'position': title,
                }
                results.append(job_data)
        # for result in results:
        #     print(result, "\n-----\n")
    return results
