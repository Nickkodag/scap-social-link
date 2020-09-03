import requests
from bs4 import BeautifulSoup

url = "https://blog.glowrecipe.com/"
r = requests.get(url)
sm_sites = ['twitter.com','facebook.com','youtube.com','instagram.com','gmail.com']
sm_sites_present = []

soup = BeautifulSoup(r.content, 'html5lib')
all_links = soup.find_all('a', href = True)


for sm_site in sm_sites:
    for link in all_links:
        if sm_site in link.attrs['href']:
            sm_sites_present.append(link.attrs['href'])

print(sm_sites_present)