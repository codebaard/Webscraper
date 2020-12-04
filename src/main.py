# prerequisites
import bs4
#from urllib.request import urlopen as uReq
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as soup
import SinglePost



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

    #username?
    #name = page_soup.findAll("a", {"class":"user-profile-name"})
    #print("Username: " + soup.prettify(name))

    lookFor = "thumb"
    results = page_soup.findAll("a", {'class':lookFor})
    #print("Found " + lookFor + ": " + str(len(results)))

    posts = list()

    #create dict from request
    for item in results:
        post = SinglePost(item.get("id")[5:], 'new', item.get("href"))
        #id = item.get("id")[5:]
        #ref = item.get("href")
        #posts[id] = ref
        posts.append(post)

    #create links and call GET
    for post in posts:
        newUrl = url + post.ref
        # make the request
        response = session.get(newUrl)
        #print("Request yielded: " + str(response.status_code))
        response.html.render(sleep=10)
        content = soup(response.html.html, "html.parser")
        print(content.prettify())

if __name__ == "__main__":

    main()