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

    try:
        session = HTMLSession()
        response = session.get(url)
        print("Request yielded: " + str(response.status_code))
        response.html.render()
    except requests.exceptions.RequestException as e:
        print(e)

    #parse html
    page_soup = soup(response.html.html, "html.parser")
    page_soup.prettify()
    #print(page_soup)

    lookFor = "container"

    containers = page_soup.findAll("div", {"class":lookFor})
    print("Found " + lookFor + ": " + str(len(containers)))
    containers = containers[2:]

    for container in containers:
        print(soup.prettify(container)) 

if __name__ == "__main__":
    main()