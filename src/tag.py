class tag(object):
    """handles the tag related data"""

    def toBSON(self):
        Tag = {
            'text'      : self.tagText,
            'category'  : self.tagCategory,
            'tagId'     : self.tagId,
            'parentPost': self.parentPostId
            }
        return Tag

    def __init__(self, text, cat, tagId, postId):
        self.tagId = tagId
        self.parentPostId = postId
        self.tagText = text
        self.tagCategory = cat