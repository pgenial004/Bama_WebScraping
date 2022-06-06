from requests import get 
from bs4 import BeautifulSoup


class craigslist:
    def __init__(self):
        pass

    def get_menu(self):
        site_source = get("https://boston.craigslist.org/search/jjj?").text
        soup = BeautifulSoup(site_source, 'html.parser')
        drop_menu = soup.find_all('li',attrs={"class": "crumb category"})
        options = drop_menu[0].find_all('option')
        list_options = {}
        
        for option in options:
            list_options[option.text] = option.attrs['value']
        return list_options

    def get_jobs(self , tag):
        site_source = get(f"https://boston.craigslist.org/search/{tag}?").text
        soup = BeautifulSoup(site_source, 'html.parser')
        rows = soup.find_all('li',attrs={"class": "result-row"})
        list_jobs = []
        for row in rows:
            text = row.find('h3',{"class":"result-heading"}).text.strip()
            link = row.find('h3',{"class":"result-heading"}).find('a')['href']
            text += " "
            try:
                text += row.find('span',{"class":"result-hood"}).text.strip()
            except:
                text += row.find('span',{"class":"nearby"}).text.strip()

            text += " ||| " + link
            list_jobs.append(text)
    
        return list_jobs

    def get_page(self , url):
        site_source = get(url).text
        soup = BeautifulSoup(site_source, 'html.parser')
        return soup.find_all('section',attrs={"id": "postingbody"})[0].text.strip()
    
    
print(craigslist().get_page("https://boston.craigslist.org/bmw/ret/d/framingham-automotive-damage-inspector/7491843365.html"))
