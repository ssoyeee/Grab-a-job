from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(keyword):
    siteUrl = "https://remoteok.com"
    url = f"{siteUrl}/remote-{keyword}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            job_td = job.find("td", class_="company")
            job_title = job_td.find("a")

            company = job_td.find("h3").string.strip()
            locations = job_td.find_all("div", class_="location")
            locations.pop(-1)
            location_str = ""
            for location in locations:
                location_str += location.string.strip() + ","
            location_str = location_str[:-1] 
            result = {
                "site": "remoteok",
                "link": f"{siteUrl}{job_title['href']}",
                "company": company,
                "location": location_str,
                "position": job_title.find("h2").string.strip()
            }
            results.append(result)
    return results
