import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York-City__2C-NY'
page = requests.get(url)

#soup is a BeautifulSoup object representing the entire web page
soup = BeautifulSoup(page.content, 'html.parser')

#results is a BeautifulSoup object containing the elements inside ResultsContainer
results = soup.find(id = 'ResultsContainer')

#job_elems is an iterable containing all the elements inside card-content
job_elems = results.find_all('section', class_="card-content")

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_= 'title')
    company_elem = job_elem.find('div', class_= 'company')
    location_elem = job_elem.find('div', class_= 'location')
    #If none is returned, ignore it
    if None in (title_elem, company_elem, location_elem):
        continue

    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()


#print(results.prettify())

