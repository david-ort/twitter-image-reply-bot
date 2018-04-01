#! usr/bin/env/python3

import os,time,json,logging,string,random,glob,search_google.api,shutil,requests
from twython import Twython,TwythonStreamer
from time import gmtime,strftime
from os import makedirs,path
from auth import *

username = 'imgReplyBOT'
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S',filename='./log.txt',filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
streamer = logging.getLogger('Streamer')
twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def img_search(query):

    buildargs = {
        'serviceName': 'customsearch',
        'version': 'v1',
        'developerKey': developerKey
    }

    cseargs = {
        'q': query,
        'cx': cx,
        'num': 4,
        'searchType': 'image',
        'fileType': 'png'
    }

    results = search_google.api.results(buildargs, cseargs)
    
    dir_path = '/home/ky/projects/Bots/imgBot/images'
    links = results.links
    key = strftime("_%d-%m-%Y_%H-%M-%S-", gmtime()) + id_generator()
    
    if not path.exists(dir_path):
        makedirs(dir_path)
    
    for i, url in enumerate(links):
        if 'start' in results.cseargs:
            i += int(results.cseargs['start'])
        ext = '.' + results.cseargs['fileType']
        file_name = results.cseargs['q'].replace(' ', '_') + '_' + str(i) + key + ext
        file_path = path.join(dir_path, file_name)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

    return key

# Streamer CLASS : IF username IS DETECTED IN THE STREAM, RESPOND WITH 4 IMAGES.
# (RESPONSE DEPENDS ON TWEET AUTHOR QUERY)
# IF SOME ERROR OCCURS, PRINT STATUS CODE AND DISCONNECT THE STREAM.

class Streamer(TwythonStreamer):

    def on_success(self, data):
        if(data['user']['screen_name'] != username):
            streamer.info('(ATTEMPT) ' + data['text'] + ' ' + data['user']['screen_name'])
            query = data['text'].split(' ',1)[1]
            reply = '@'+data['user']['screen_name'] + ' ' + query

            key = img_search(query)
            files = glob.glob('/home/ky/projects/Bots/imgBot/images/*' + key + '.png')
            ids = []
            for i in files:
                photo = open(i, 'rb')
                response = twitter.upload_media(media=photo)
                ids.append(response['media_id'])
            twitter.update_status(status=reply,in_reply_to_status_id=data['id_str'],media_ids=ids)
            streamer.info('(POSTED) ' + data['text'] + data['user']['screen_name'])


    def on_error(self, status_code, data):
        streamer.error(status_code + data['text'] + data['user']['screen_name'])
        self.disconnect()

# main() : STARTS OFF THE TWITTER STREAM (TRACKING BY USERNAME).

def main():

    stream = Streamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=username)

    return 0

main()
