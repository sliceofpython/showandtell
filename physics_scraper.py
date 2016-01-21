"""
www.phys.org scraper
by VR29

TODO:
- support references
"""

import requests
import bs4

base_url = 'http://phys.org/physics-news/'
r = requests.get(base_url)
soup = bs4.BeautifulSoup(r.text, 'html.parser')

artikelen = {}

titles = soup.select("h3 > a")

#print(titles[0].get('href'))



def get(url):
    get_url = url
    r_get = requests.get(get_url)
    soup_get = bs4.BeautifulSoup(r_get.text, 'lxml')
    print("----------------------", file=file_text)
    print(soup_get.select(".content-head > h1")[0].text.strip(), file=file_text)
    print(file=file_text)
    print(soup_get.select(".content-head > h5")[0].text.strip(), file=file_text)
    print(file=file_text)
    print(soup_get.select(".first-block")[0].text.strip(), file=file_text)
    for i in range(len(soup_get.select("article > p"))):
        print(soup_get.select("article > p")[i].text.strip(), file=file_text)
        print(file=file_text)

def article():
    for x in range(0, 10):
        get(titles[x].get('href'))

file_text = open('physics.txt','w')
article()
print("Output to " + file_text.name + " finished!")
file_text.close()

