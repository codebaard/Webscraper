
# this class is made to represent the basic shape of the requested or scraped content
# based on the scraped webpage, this can be altered and should be ultimately the only part which is changed
# alongside database and user credential properties

class SinglePost:

    def __init__(self, id, cat, ref):

        self.postId = id
        self.category = cat
        self.href = ref

    def setVotes(self, upVotes, downVotes, benis):
        self.benis = benis
        self.upVotes = upVotes
        self.downVotes = downVotes

    def setComments(self, commentCount):
        self.commentCount = commentCoung

    def setTagCount(self, tagCount):
        self.tagCount = tagCount
 
