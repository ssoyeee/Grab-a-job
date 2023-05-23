from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("can't request website")
else:
    print(response.text)

