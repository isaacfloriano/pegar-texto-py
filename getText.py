import requests
from bs4 import BeautifulSoup

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
p = soup.find_all('h1')[0].get_text()
print(p)

# fontes: 
#	https://www.digitalocean.com/community/tutorials/como-trabalhar-com-dados-da-web-usando-requests-e-beautiful-soup-com-python-3-pt


