from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os

def download_file(url, filename):
        response = uReq(url)
        file = open(filename, 'wb')
        file.write(response.read())
        file.close()
        response.close()

page_url = "https://database.lichess.org/"
uClient = uReq(page_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
downloadlinks = page_soup.findAll("a", text=".pgn.bz2")
for element in reversed(downloadlinks):
    link = element["href"]
    if(link[:9] == "standard/"):
        print("downloading: " + page_url + link + " as: " + link[9:])
        folder = link[:9]
        if not os.path.exists(folder):
            os.mkdir(folder)
        download_file(page_url + link, link)

