import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page


def extract_indeed_jobs(last_page):
    jobs = []

    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0 * LIMIT}")
    print(f"{URL}&start={0 * LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')

    job_card = soup.find(id="mosaic-provider-jobcards")
    results = job_card.find_all("div", {"class": "job_seen_beacon"})

    for result in results:
        titles = result.find("h2", {"class": "jobTitle"}).find_all("span")
        title = titles[0].get('title')

        if title is None:
            title = titles[1].get('title')

        company = result.find("span", {"class": "companyName"})
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company.strip()

        print(title, company)

    return jobs
