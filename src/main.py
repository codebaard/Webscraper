# prerequisites
import bs4
#from urllib.request import urlopen as uReq
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as soup

def main():

    # make the request
    #url = "https://pr0gramm.com"
    url = "https://cms.hotpot.codes/AssetShowcase/Index"
    #uClient = uReq(url)
    session = HTMLSession()
    request = session.get(url)
    print(request.status_code)
    #r.headers['content-type']
    #r.encoding
    #r.json()

    #render js
    request.html.render()
    #print(request.html.text)
    #content.html.text

    #parse html
    page_soup = soup(request.html.text, "html.parser")
    print(page_soup)


if __name__ == "__main__":
    main()