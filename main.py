from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs


keyword = input("What do you want to search for? ")
if keyword is None:
    raise ValueError("The value is incorrect.")
else:
    print(f"Keyword: {keyword}")

indeed = extract_indeed_jobs(keyword) # return list
wwr = extract_wwr_jobs(keyword) # return list

jobs = indeed+wwr

file = open(f"{keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")


for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
file.close()

