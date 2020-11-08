import requests
from bs4 import BeautifulSoup
from LogPython import LogManager

resp = requests.get("https://start.bizon365.ru/room/16650/bachelorsmeeting?utm_source=&utm_medium=&utm_campaign=&utm_term=&utm_content=").text
_soup = BeautifulSoup(resp, "lxml")

print(_soup.title)

res = _soup.find_all("li")

print(res)