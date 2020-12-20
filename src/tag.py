from JSONAble import JSONAble

class tag(JSONAble):
    """handles the tag related data"""

    def __init__(self, text, cat, tagId, postId):
        self.tagId = tagId
        self.parentPostId = postId
        self.tagText = text
        self.tagCategory = cat


