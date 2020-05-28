import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York-City__2C-NY'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

