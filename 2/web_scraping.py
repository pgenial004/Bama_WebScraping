from requests import get 
from bs4 import BeautifulSoup
import json

class Bing:
    def __init__(self):
        pass

    def image_search(self, text , count = 20):
        site_source = get(f"https://www.bing.com/images/async?q={text}&first=0&count={count}&cw=1177&ch=696&relp=35&tsc=ImageHoverTitle&datsrc=I&layout=RowBased&mmasync=1",
        headers={'Host': 'www.bing.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0', 'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}).text
        soup = BeautifulSoup(site_source, 'html.parser')
        images = soup.find_all('a',attrs={"class": "iusc"})
        list_images = []
        for image in images:
            y = json.loads(image.attrs['m'])
            list_images += y["murl"]

Bing().image_search("ali%20reza")


