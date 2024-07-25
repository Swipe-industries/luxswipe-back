class User:
    def __init__(self, username, uid, name, bio=None, catagory=None, followers=0, posts=0):
        self.username = username
        self.uid = uid
        self.name = name
        self.bio  = bio
        self.catagory = catagory
        self.followers = followers
        self.posts = posts