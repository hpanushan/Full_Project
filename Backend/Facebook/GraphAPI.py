import requests
from Credentials import pageAccessToken

class GraphAPI:

    def __init__(self, access_token):
        self.access_token = access_token

    def getPageID(self):
        # Get the id of the page
        url = "https://graph.facebook.com/v3.3/me?access_token={}".format(self.access_token)
        result = requests.get(url).json()
        return result['id']

    def getPageName(self):
        # Get the name of the page
        url = "https://graph.facebook.com/v3.3/me?access_token={}".format(self.access_token)
        result = requests.get(url).json()
        return result['name']

    def getPagePostsList(self,pageID):
        # Get the list of posts of the page
        url = "https://graph.facebook.com/v3.3/{}/feed?access_token={}".format(pageID,self.access_token)
        result = requests.get(url).json()
        return result['data']

    def getPostCommentsList(self,postID):
        # Get the list comments of the specific post
        url = "https://graph.facebook.com/v3.3/{}/comments?access_token={}".format(postID,self.access_token)
        result = requests.get(url).json()
        return result['data']


