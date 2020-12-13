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
            print(post.postId + " has no public vote count yet")            

        try:
            tags = content.findAll("span", {"class":"tag"})
            #tags = re.findall(r'\d+', benis[0].attrs["title"])
            post.setTagCount(len(tags))
        except:
            print("smth wrong with tags...")

        try:
            print(str(post.postId) + " has " + str(post.benis) + " benis, " + str(post.commentCount) + " comments and " + str(post.tagCount) + " tags.")
        except:
            print(str(post.postId) + " has no public benis, " + str(post.commentCount) + " comments and " + str(post.tagCount) + " tags.")

if __name__ == "__main__":
    main()