#Consumer key 	kK38G4kaJ96PjsTVeLydA
#Consumer secret 	yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY
#Request token URL 	https://api.twitter.com/oauth/request_token
#Authorize URL 	https://api.twitter.com/oauth/authorize
#Access token URL 	https://api.twitter.com/oauth/access_token

#Access token 	2198562481-an7PLZDdY1SIS8Ck0HHTBBoaNUVIJKw2vhLnLBb
#Access token secret 	mdey7QqzlHSDNDOKWBXz1MwMNX6LeBUdzAC15AHe8d6xz
#Access level 	Read-only

from twython import Twython

APP_KEY = kK38G4kaJ96PjsTVeLydA
APP_SECRET = yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
