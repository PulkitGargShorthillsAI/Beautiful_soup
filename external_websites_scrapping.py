from bs4 import BeautifulSoup
import requests


def scrapping():
    html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('div',class_="srp-listing clearfix")
    for job in jobs:
        # print(job.prettify())
        company_name = job.find('h4').find('span',class_="srp-comp-name").text
        info = job.find('a')['href']
        skills = job.find_all('a',class_="srphglt")

        print('Company name :',company_name)
        skill_arr = ""
        
        for skill in skills:
            skill_arr += skill.text + ','
        print("Skills : ",skill_arr)
        print(f"For more info : {info}")
        print(f'\n\n\n')


scrapping()