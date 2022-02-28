import requests
from bs4 import BeautifulSoup
import csv

BASEURL = 'https://hu.indeed.com/jobs'
what = input('What jobs to search: ')
where = input('Where to search: ')
tup_in = what, where

if tup_in == ():
    tup_in = ('python', 'budapest')


def get_links(params_in, pages=1):
    """ Compiles a list of job description links"""
    joblist = []
    for p in range(pages):
        params = f'?q={params_in[0]}&l={params_in[1]}&start={p * 10}'
        response = requests.get(BASEURL + params)
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find(id='mosaic-provider-jobcards').find_all('a')
        # jobs[0]['href'] - a relative link to the full text
        for job in jobs:
            if 'rc/clk?' in job['href']:
                description_link = 'https://hu.indeed.com' + job['href']
                joblist.append(description_link)
    print(f'{len(joblist)} links were collected')
    return joblist


def fill_dict(list_of_links):
    """Turns a link of job description into a list of dictionaries """
    list_of_dict = []
    for job in list_of_links:
        jobdict = {}
        response = requests.get(job)
        soup = BeautifulSoup(response.text, 'html.parser')
        jobdict['job_title'] = soup.find('h1').text
        jobdict['company_location'] = soup.find(class_='jobsearch-CompanyInfoContainer').text
        #TODO find out how to write Hungarian Unicode to the csv file
        jobdict['job_description'] = soup.find(id='jobDescriptionText').text.encode("utf8")
        list_of_dict.append(jobdict)
    print(f'{len(list_of_dict)} job descriptions added to the dictionary')
    return list_of_dict


def write_to_file(job_links_list):
    with open('jobs.csv', 'w', newline='') as f:
        headers = ['job_title', 'company_location', 'job_description']
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(job_links_list)
    print('jobs written to "jobs.csv"')


links = get_links(tup_in, 5)
joblist = fill_dict(links)
write_to_file(joblist)
