# prerequisites
import bs4
#from urllib.request import urlopen as uReq
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as soup
from databaseHandler import databaseHandler
from SinglePost import SinglePost
import re
from bson import BSON

def main():

    mongo = databaseHandler()

    # use https://www.youtube.com/watch?v=QoyIWDKrWU0 for login and filter process
    #https://medium.com/level-up-programming/how-to-scrap-data-from-javascript-based-website-using-python-selenium-and-headless-web-driver-531c7fe0c01f
    #https://github.com/SeleniumHQ/docker-selenium

    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en,de-DE;q=0.9,de;q=0.8,en-US;q=0.7", 
    "Cache-Control": "max-age=0", 
    "Dnt": "1", 
    "Host": "pr0gramm.com", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.400"
    }

    try:
        # make the request
        url = "https://pr0gramm.com"
        #url = "http://httpbin.org/get"
        session = HTMLSession()
        response = session.get(url, headers = headers)
        #response = session.get(url)
        #print("Request yielded: " + str(response.status_code))
        response.html.render()
    except requests.exceptions.RequestException as e:
        print(e)

    #parse html
    page_soup = soup(response.html.html, "html.parser")

    #print page 
    #print(page_soup.prettify())

    lookFor = "thumb"
    results = page_soup.findAll("a", {'class':lookFor})
    #print("Found " + lookFor + ": " + str(len(results)))

    posts = list()

    #create list of posts
    for item in results:
        posts.append(SinglePost(item.get("id")[5:], 'new', item.get("href")))

    #create links and call GET
    for post in posts:
        newUrl = url + post.href
        # make the request
        response = session.get(newUrl)
        #print("Request yielded: " + str(response.status_code))
        response.html.render(sleep=0.1)
        content = soup(response.html.html, "html.parser")
        try:
            benis = content.find("div", {'class':'item-vote'}).findChildren("span", {"class":"score"})
        except:
            print("post deleted...?!")

        try:
            comments = content.find("div", {"class":"comments-head"})
            cCount = re.findall(r'\d+', comments.text)
            post.setComments(cCount[0])
        except:
            post.setComments(0)

        try:
            votes = re.findall(r'\d+', benis[0].attrs["title"])
            post.setVotes(votes[0], votes[1], benis[0].contents[0])
        except:
            post.setVotes('not public', 'not public', 'not public')           

        try:
            tags = content.findAll("span", {"class":"tag"})
            for tag in tags:
                post.addTag(tag)
        except:
            print("smth wrong with tags...")

        try:
            comments = content.findAll("div", {"class":"comment"})
            for comment in comments:
                post.addComment(comment)
        except:
            print("no comments prb :-(")

        #try:
        #    print(str(post.postId) + " has " + str(post.benis) + " benis, " + str(post.commentCount) + " comments and " + str(len(post.tags)) + " tags.")
        #except:
        #    print(str(post.postId) + " has no public benis, " + str(post.commentCount) + " comments and " + str(len(post.tags)) + " tags.")

        #mongo.db.posts.insert_one(BSON.encode(post.toJSON()))
        #print(post.toJSON())

if __name__ == "__main__":
    main()