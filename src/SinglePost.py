from tag import tag 
from JSONAble import JSONAble
# this class is made to represent the basic shape of the requested or scraped content
# based on the scraped webpage, this can be altered and should be ultimately the only part which is changed
# alongside database and user credential properties

class SinglePost(JSONAble):

    def __init__(self, id, cat, ref):
        self.tags = list()
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