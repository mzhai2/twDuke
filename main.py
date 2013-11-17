from twython import Twython
import sys
sys.argv

target = open('f.txt', "wb")
APP_KEY = 'kK38G4kaJ96PjsTVeLydA'
APP_SECRET = 'yLFu9sgN7Bw0e3QWuXzHzOts9zkPaojmRRVDnNE8vhY'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token = ACCESS_TOKEN)

target.write(str(twitter.search(q=@sys.argv[0]', result_type='recent')))

target.close()