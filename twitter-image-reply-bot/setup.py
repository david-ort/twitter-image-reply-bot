#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import modules
import google_images_search,logging,os
from threading import Thread
from twython import Twython,TwythonStreamer

# twitter handle
handle = "img_reply_bot"    # doesn't require "@"
# twitter API keys
api_key = ""
api_secret = ""
oauth_token = ""
oauth_token_secret = ""

# google custom search API keys
cx = ""
google_api_key = ""

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

