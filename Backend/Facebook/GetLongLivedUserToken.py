# To get long-lived access token

import requests
import Credentials

def getLongLivedUserToken():
    app_id = Credentials.AppID
    app_secret = Credentials.AppSecret
    user_short_token = Credentials.ShortLivedUserToken
    access_token_url = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(app_id, app_secret, user_short_token)

    r = requests.get(access_token_url)

    access_token_info = r.json()
    user_long_token = access_token_info['access_token']
    return user_long_token

print(getLongLivedUserToken())

