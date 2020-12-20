from JSONAble import JSONAble

class comment(JSONAble):
    """comment class"""

    def __init__(self, commentId, parentCommentId, content, upVotes, downVotes, benis, timestamp, isOP, username):
        self.commentId = commentId
        self.parentCommentId
        self.content = content
        self.upVotes = upVotes
        self.downVotes = downVotes
        self.benis = benis
        self.timestamp = timestamp
        self.isOP = isOP
        self.username = username


