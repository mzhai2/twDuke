#Consumer key 	kK38G4kaJ96PjsTVeLydA
#Consumer secret 	yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY
#Request token URL 	https://api.twitter.com/oauth/request_token
#Authorize URL 	https://api.twitter.com/oauth/authorize
#Access token URL 	https://api.twitter.com/oauth/access_token

#Access token 	2198562481-an7PLZDdY1SIS8Ck0HHTBBoaNUVIJKw2vhLnLBb
#Access token secret 	mdey7QqzlHSDNDOKWBXz1MwMNX6LeBUdzAC15AHe8d6xz
#Access level 	Read-only

from twython import Twython
from twython import TwythonStreamer
import sys, getopt

APP_KEY = 'kK38G4kaJ96PjsTVeLydA'
APP_SECRET = 'yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=1)

auth = twitter.get_authentication_tokens(callback_url='http://www.emorywiki.com')
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# print 'https://api.twitter.com/oauth/authorize?oauth_token='+OAUTH_TOKEN;
print auth['auth_url']
# twitter.search(q='python')
#search = twitter.search_gen('python')
#for result in search:
#    print result

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()

stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='twitter')