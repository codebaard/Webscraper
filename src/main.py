# prerequisites
import bs4
#from urllib.request import urlopen as uReq
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as soup

def main():

    try:
        # make the request
        url = "https://pr0gramm.com"
        session = HTMLSession()
        response = session.get(url)
        #print("Request yielded: " + str(response.status_code))
        response.html.render()
    except requests.exceptions.RequestException as e:
        print(e)

    #parse html
    page_soup = soup(response.html.html, "html.parser")

    #print whole page html
    # print(page_soup.prettify())

    #username?
    #name = page_soup.findAll("a", {"class":"user-profile-name"})
    #print("Username: " + soup.prettify(name))

    lookFor = "thumb"
    results = page_soup.findAll("a", {'class':lookFor})
    #print("Found " + lookFor + ": " + str(len(results)))

    #firstItem = results[0]
    #latestId = firstItem.get("id")[5:]
    #print(latestId)

    posts=dict()

    #create dict from request
    for item in results:
        id = item.get("id")[5:]
        ref = item.get("href")
        posts[id] = ref

    #create links and call GET
    (k,v)  = posts.popitem()

    #newUrl = url + posts[post]   
    newUrl = url + v
    #print(newUrl)
    # make the request
    response = session.get(newUrl)
    #print("Request yielded: " + str(response.status_code))
    response.html.render(sleep=10)
    content = soup(response.html.html, "html.parser")
    print(content.prettify())

if __name__ == "__main__":
    main()