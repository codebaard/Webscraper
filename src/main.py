# prerequisites
import bs4
#from urllib.request import urlopen as uReq
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as soup
from SinglePost import SinglePost
import re



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
        newUrl = url + post.href
        # make the request
        response = session.get(newUrl)
        #print("Request yielded: " + str(response.status_code))
        response.html.render(sleep=1)
        content = soup(response.html.html, "html.parser")
        benis = content.find("div", {'class':'item-vote'}).findChildren("span", {"class":"score"})
        votes = re.findall(r'\d+', benis[0].attrs["title"])
        post.setVotes(post, votes[0], votes[1], benis[0].contents[0])
        #print(content.prettify())
        print(post.postId + " has " + post.benis + " benis")

if __name__ == "__main__":

    main()