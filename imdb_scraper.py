# IMDB scraper
# By: VR29

import requests, bs4

movie_rating = {}

res = requests.get('http://www.imdb.com/chart/toptv/?ref_=nv_tp_tv250_2')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")

name = soup.select('.lister-list > tr:nth-of-type(1) > td:nth-of-type(2) > a:nth-of-type(1)')
rating = soup.select('.lister-list > tr:nth-of-type(1) > td:nth-of-type(3) > strong:nth-of-type(1)')

for x in range(1,250):
    name = soup.select('.lister-list > tr:nth-of-type(' + str(x) + ') > td:nth-of-type(2) > a:nth-of-type(1)')
    rating = soup.select('.lister-list > tr:nth-of-type(' + str(x) +') > td:nth-of-type(3) > strong:nth-of-type(1)')
    movie_rating[name[0].text] = rating[0].text

print (movie_rating)