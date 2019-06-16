import urllib.request
from bs4 import BeautifulSoup


def get(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
    req = urllib.request.Request(url, headers = headers)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'lxml')
    return(soup)
   
def find():
    