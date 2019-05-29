import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(response.text, 'html.parser')

newsList = soup.find_all(class_='athing')

with open('news.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['title', 'link']
    csv_writer.writerow(headers)

    for news in newsList:
        title = news.find(class_='storylink').get_text()
        link = news.find('a')['href']
        csv_writer.writerow([title, link])
