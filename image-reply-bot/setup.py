#  Author       : David J. Ortiz Rivera / kytrnd / STILLinBL00M
#  Project      : Twitter Image Reply BOT
#  File         : setup.py
#  Description  : Imports all modules and initializes Twitter handle, API keys, and logger.

import json,string,random,glob,search_google.api,shutil,requests,logging
from twython import Twython,TwythonStreamer
from time import gmtime,strftime
from os import makedirs,path

#  Twitter handle and API keys

handle = 'your_handle' # Does not require '@'
app_key = 'your_app_key'
app_secret = 'your_app_secret'
oauth_token = 'your_oath_token'
oauth_token_secret = 'your_oauth_token_secret'

#  Google Custom Search API keys

developerKey = 'your_developerKey'
cx = 'your_cx'

#  Logger setup

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%d-%m-%y %H:%M:%S',filename='./bot.log',filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
streamer = logging.getLogger('Streamer')
search = logging.getLogger('img_search')
