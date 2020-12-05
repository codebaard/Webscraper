
# this class is made to represent the basic shape of the requested or scraped content
# based on the scraped webpage, this can be altered and should be ultimately the only part which is changed
# alongside database and user credential properties

class SinglePost:

    #postId
    #category
    #href
    #benis

    def __new__(self, id, cat, ref):

        self.postId = id
        self.category = cat
        self.href = ref

        return self

    def setVotes(self, upVotes, downVotes, benis):
        self.benis = benis
        self.upVotes = upVotes
        self.downVotes = downVotes


 
