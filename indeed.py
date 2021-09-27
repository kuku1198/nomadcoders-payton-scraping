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


def extract_job(html):
    titles = html.find("h2", {"class": "jobTitle"}).find_all("span")
    title = titles[0].get('title')

    if title is None:
        title = titles[1].get('title')

    company = html.find("span", {"class": "companyName"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company.strip()

    location = html.find("div", {"class": "companyLocation"}).get_text()
    job_id = html.find_parent("a")["data-jk"]

    return {
        'title': title,
        'company': company,
        'location': location,
        "link": f"https://www.indeed.com/viewjob?jk={job_id}"
    }


def extract_indeed_jobs(last_page):
    jobs = []

    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')

        job_card = soup.find(id="mosaic-provider-jobcards")
        results = job_card.find_all("div", {"class": "job_seen_beacon"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs
