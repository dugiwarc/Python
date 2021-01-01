from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://fr.indeed.com/jobs?q=React&l=France').text

soup = BeautifulSoup(html_text, 'html.parser')

job = soup.find(
    'div', class_='jobsearch-SerpJobCard')

job_title = job.find('h2', class_="title").text.replace(" ", "")
summary = job.find("div", class_="summary")
summary_desc = summary.find('li').text
print(summary_desc)
