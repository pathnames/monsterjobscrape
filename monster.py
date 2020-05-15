import requests

url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York-City__2C-NY'
page = requests.get(url)

print(page.content)