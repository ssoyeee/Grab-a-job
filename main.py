from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file


keyword = input("What do you want to search for? ")
if keyword is None:
    raise ValueError("The value is incorrect.")
else:
    print(f"Keyword: {keyword}")

indeed = extract_indeed_jobs(keyword) # return list
wwr = extract_wwr_jobs(keyword) # return list

jobs = indeed+wwr

save_to_file(keyword, jobs)