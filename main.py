from twython import Twython
import sys
sys.argv
search = '@'
search += str(sys.argv[1])
if len(sys.argv) == 3:
	search += '@'
	search += str(sys.argv[2])
if len(sys.argv) == 4:
	search += '@'
	search += str(sys.argv[3])
if len(sys.argv) == 5:
	search += '@'
	search += str(sys.argv[4])
print search
target = open('f.json', "wb")
APP_KEY = 'kK38G4kaJ96PjsTVeLydA'
APP_SECRET = 'yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token = ACCESS_TOKEN)

target.write(str(twitter.search(q=search, result_type='recent')))

target.close()