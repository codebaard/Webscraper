from tag import tag 
from comment import comment
from JSONAble import JSONAble
import re
# this class is made to represent the basic shape of the requested or scraped content
# based on the scraped webpage, this can be altered and should be ultimately the only part which is changed
# alongside database and user credential properties

class SinglePost(JSONAble):

    def __init__(self, id, cat, ref):
        self.tags = list()
        self.comments = list()
        self.postId = id
        self.category = cat
        self.href = ref

    def setVotes(self, upVotes, downVotes, benis):
        self.benis = benis
        self.upVotes = upVotes
        self.downVotes = downVotes

    def setComments(self, commentCount):
        self.commentCount = commentCount

    def addTag(self, tagObject):
        text = tagObject.findChild().text
        tagCat = tagObject.attrs["class"][1]
        tagId = tagObject.attrs["id"]
        newTag = tag(text, tagCat, tagId, self.postId)
        self.tags.append(newTag)

    def addComment(self, commentObject):
        #id = commentObject.attrs["id"]
        #parent = "none"
        content = commentObject.contents[3].text
        print(content)
        #footer = commentObject.contents[5]
        #upVotes, downVotes = re.findall(r'\d+', votes.attrs["title"])
        #benis = votes.text
        #timestamp = commentObject.contents[5].contents[0][5].attrs["title"]
        #try:
        #    op = commentObject.span["user-comment-op"].text
        #except:
        #    op = False

        #print("just for debugging")
