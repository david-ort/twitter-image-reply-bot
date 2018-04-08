#  Author       : David J. Ortiz Rivera / kytrnd / STILLinBL00M
#  Project      : Twitter Image Reply BOT (https://github.com/kytrnd/Image-Reply-Bot)
#  File         : img_reply_bot.py
#  Description  : Replies to a Twitter user with a query-based png album.
#  Version      : 1.0.0

from auth import *

# id_generator(size,chars) : Creates an id to help differentiate images.
#                          : The id consists of uppercase ascii caracters and digits.

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# img_search(query): Downloads 4 query-based png images to dir_path.

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

    search.info('Attempt (' + query + ')')
    results = search_google.api.results(buildargs, cseargs)
    links = results.links
    key = id_generator()
    
    # Images will be saved in this path.
    dir_path = 'your_path'    
    if not path.exists(dir_path):
        makedirs(dir_path)

    # Name and save each image. 
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
    search.info('Success (' + query + ')')
    return key

# Streamer Class : 
#   on_success(self,data)           : If @handle is detected in stream, log and respond with 4 png images.
#   on_error(self,status_code,data) : If some error occurs, log it, print status code, and disconnect the stream.

class Streamer(TwythonStreamer):

    def on_success(self,data):
        if(data['user']['screen_name'] != handle): # Validates input and prevents a reply to itself
            streamer.info('Attempt (User: ' + data['user']['screen_name'] + 'Query: ' + data['text'] + ')')
            twitter = Twython(app_key,app_secret,oauth_token,oauth_token_secret)
            query = data['text'].split()
            tmp = ''
            for i in query:
                if '@' not in i:
                    tmp += i + ' '
            tmp = tmp[:-1]
            
            reply = '@'+data['user']['screen_name'] + ' ' + tmp
            key = img_search(tmp)

            # Obtaining paths for images to be posted.
            files = glob.glob('your_path/*' + key + '.png')
            ids = []
            
            # Upload images onto twitter.
            for i in files:
                photo = open(i, 'rb')
                response = twitter.upload_media(media=photo)
                ids.append(response['media_id'])
            twitter.update_status(status=reply,in_reply_to_status_id=data['id_str'],media_ids=ids)
            streamer.info('Success (User: ' + data['user']['screen_name'] + 'Query: ' + data['text'] + ')')

    def on_error(self,status_code,data):
        streamer.error(status_code)
        self.disconnect()

# main() : Starts off the twitter stream (tracking by handle).

def main():
    streamer.info('Streamer started')
    stream = Streamer(app_key,app_secret,oauth_token,oauth_token_secret)
    stream.statuses.filter(track=handle)
    return 0

main()
