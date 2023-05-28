from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("can't request website")
else:
    #print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find_all('section', class_="jobs"))



