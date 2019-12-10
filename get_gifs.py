import requests
from bs4 import BeautifulSoup
import urllib

page = requests.get('https://www.spotebi.com/exercise-guide/')
soup = BeautifulSoup(page.text, 'html.parser')
a = soup.find(class_ = 'grids-frame').find_all('li')
now = 1
for elem in a:
    url = elem.find('a').get('href')
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    url = soup.find_all('meta', property="og:image")[0]['content'][:-3] + "gif"
    try:
        print(url)
        urllib.request.urlretrieve(url, "C:/Users/79263/Keep Fit/{}.gif".format(now))
        now += 1
    except:
        print('error')
    
