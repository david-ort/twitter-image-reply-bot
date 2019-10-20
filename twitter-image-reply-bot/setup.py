#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import modules
import google_images_search,logging,os
from threading import Thread
from twython import Twython,TwythonStreamer

# twitter handle
handle = "img_reply_bot"    # doesn't require "@"
# twitter API keys
api_key = "GTW8xPtwWBqo8LrLXNgfmb8tC"
api_secret = "5WaLwGmnSgLTVjnVSwrUuJC6qvy8q2MPskCxoFaJFvDbuUgGn8"
oauth_token = "938172754691584001-lBqCACvL4bFLnnLqcFRWcUBTBwuuHV4"
oauth_token_secret = "PH0NVLYUYmh8AscMGsbq5p4rVRWXZ0KiZbbeL31c0NEUt"

# google custom search API keys
cx = "003155942714465478666:a3phhqg2xgo"
google_api_key = "AIzaSyDvpeEfdyZZIFqgEQ2Gmw5q5LkJN54CnBQ"

# logger format
date_fmt = "%Y-%m-%d %H:%M:%S"
fmt = "%(asctime)s: %(name)s %(message)s"
# configure logger
logging.basicConfig(level=logging.INFO,format=fmt,datefmt=date_fmt,filename="bot.log",filemode="a")
# set image and stream loggers
image_log = logging.getLogger("(image)")
stream_log = logging.getLogger("(stream)")
# set console logger
console = logging.StreamHandler()
console.setFormatter(logging.Formatter(fmt,date_fmt))
logging.getLogger("").addHandler(console)

