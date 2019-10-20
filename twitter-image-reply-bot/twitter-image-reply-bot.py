#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import api keys
from setup import *

#  get_id(img: int): upload image and save media id
def get_id(img):
    image = gis.results()[img]
    # get image as raw data
    raw_img = image.get_raw_data()
    data = twitter.upload_media(media=raw_img)
    ids[img] = data["media_id"]

# img_search(query: string): fetch 4 query-based images
def img_search(query):
    image_log.info("query attempt {%s}" % (query))
    # set search parameters
    search_params = {"q": query,"num": 4,"safe": "off","fileType": "png"}
    # search images
    gis.search(search_params=search_params,cache_discovery=False)
    # fetch media ids using multithreading
    threads = []
    # create threads 
    for img in range(0,len(gis.results())):
        thread = Thread(target=get_id,args=[img])
        threads.append(thread)
        thread.start() 
    # block until all ids are fetched
    for thread in threads:
        thread.join()
    
    image_log.info("query success {%s}" % (query))

# get_query(tweet: string): extract query from tweet by removing all handles
def get_query(tweet):
    tweet = tweet.split()
    for word in tweet:
        # remove handles
        if "@" in word:
            tweet.remove(word)
    # return query
    return " ".join(tweet)

class Streamer(TwythonStreamer):
    # on_success(self: streamer,data: json): if handle and query is detected in stream, respond with query album
    def on_success(self,data):
        # extract tweet data from response
        tweet = data["text"]
        reply_id = data["id_str"]
        reply_handle = data["user"]["screen_name"]      
        stream_log.info("query attempt {%s}" % (tweet))

        # like tweet
        if "good bot" in tweet.lower():
            twitter.create_favorite(id=reply_id)
        # album reply, avoid self-reply
        if(reply_handle != handle):
            # extract query from tweet
            query = get_query(tweet)
            # avoid null queries
            if query:
                img_search(query)
                reply = ("@%s %s %s" % (reply_handle,query ,"🐸"))
                # respond with album
                twitter.update_status(status=reply,in_reply_to_status_id=reply_id,media_ids=ids)
                stream_log.info("query successful {%s}" % (tweet))

    # on_error(self: streamer,status_code: int,data: json): when non-200 status code is received, disconnect the stream
    def on_error(self,status_code,data):
        stream_log.error("error %s",(status_code))
        self.disconnect()
        # terminate
        os._exit(-1)

# main() : initialize stream, filter by handle
def main():
    # initialize stream
    streamer.statuses.filter_async(track=handle)
    stream_log.info("initialized")
    # end stream on "enter"
    input("")
    # streamer.disconnect()
    stream_log.info("disconnected")
    return 0

# initialize instances/stream
if __name__ == "__main__":
    # save media ids globally
    ids = {}
    # create instances
    gis = google_images_search.GoogleImagesSearch(google_api_key,cx)
    twitter = Twython(api_key,api_secret,oauth_token,oauth_token_secret)
    streamer = Streamer(api_key,api_secret,oauth_token,oauth_token_secret)
    # initialize stream
    main()
