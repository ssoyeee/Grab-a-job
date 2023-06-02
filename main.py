from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for? ")
 
indeed = extract_indeed_jobs(keyword) # return list
wwr = extract_wwr_jobs(keyword) # return list

jobs = indeed+wwr

for job in jobs:
    print(job)
    print("//////\n//////")

