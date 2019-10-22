import facebook, urllib3, requests
import Credentials

def getPermanentPageAccessToken():
    token = Credentials.LongLivedUserToken
    graph = facebook.GraphAPI(access_token=token)
    pages_data = graph.get_object("/me/accounts")
    return pages_data['data'][0]["access_token"]

print(getPageAccessToken())
