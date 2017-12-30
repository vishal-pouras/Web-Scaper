import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import csv

r = requests.get('http://coreyms.com')

soup = BeautifulSoup(r.content, 'lxml')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video-link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', {'class' : 'entry-content'}).p.text
    print(summary)


    try:
        vid_src = article.find('iframe', {'class' : 'youtube-player'})['src']
        o = urlparse(vid_src)
        yt_link = o.scheme + "://" + o.netloc + o.path
        print(yt_link)
    except Exception as e:
        print("NONE")
    print()

    csv_writer.writerow([headline, summary, yt_link])
