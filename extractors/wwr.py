from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
   # search_term = "python" # search keyword
    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("can't request website")
    else:
        #print(response.text)
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all('li') # list of lis
            job_posts.pop(-1)
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company, jobtype, region = anchor.find_all('span', class_="company")
                title = anchor.find('span', class_="title")
                job_data = {
                    'link': f"https://weworkremotely.com{link}",
                    'company': company.string,
                    'jobtype': jobtype.string,
                    'location': region.string,
                    'position': title.string
                }
                results.append(job_data)
        return results



