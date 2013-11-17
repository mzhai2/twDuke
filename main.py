#Consumer key 	kK38G4kaJ96PjsTVeLydA
#Consumer secret 	yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY
#Request token URL 	https://api.twitter.com/oauth/request_token
#Authorize URL 	https://api.twitter.com/oauth/authorize
#Access token URL 	https://api.twitter.com/oauth/access_token

#Access token 	2198562481-an7PLZDdY1SIS8Ck0HHTBBoaNUVIJKw2vhLnLBb
#Access token secret 	mdey7QqzlHSDNDOKWBXz1MwMNX6LeBUdzAC15AHe8d6xz
#Access level 	Read-only

from twython import Twython

<<<<<<< HEAD
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()

APP_KEY = 'kK38G4kaJ96PjsTVeLydA'
APP_SECRET = 'yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY'

twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()


OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['auth_url']
print OAUTH_TOKEN
print OAUTH_TOKEN_SECRET


oauth_verifier = raw_input()

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
final_step = twitter.get_authorized_tokens('oauth_verifier')
print final_step
OAUTH_TOKEN = final_step[OAUTH_TOKEN]
OAUTH_TOKEN_SECERT = final_step[OAUTH_TOKEN_SECRET]

# twitter.search(q='python')
#search = twitter.search_gen('python')
#for result in search:
#    print result

#stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#stream.statuses.filter(track='twitter')
=======
APP_KEY = 'kK38G4kaJ96PjsTVeLydA'
APP_SECRET = 'yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token = ACCESS_TOKEN)

twitter.search(q='python', result_type='popular')
>>>>>>> parent of 541ff6e... streamer ex
