# Twitter Image Reply Bot

This script obtains user mentions via Twython, a Python wrapper for the Twitter API and replies with 4 query-based png images obtained through the search_google, a module for Google API image search.

## Getting Started

1. [Create a Twitter account](https://www.google.com.pr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=13&cad=rja&uact=8&ved=0ahUKEwiTtKCX-afaAhUMq1kKHbdJCfIQFghhMAw&url=https%3A%2F%2Ftwitter.com%2Fsignup%3Flang%3Den&usg=AOvVaw1MfJ_wTmLtjRlnLzZ8bNkM)
2. [Create a Twitter application](http://docs.inboundnow.com/guide/create-twitter-application/)
3. [Create your Custom Search Engine with Google](https://developers.google.com/custom-search/docs/tutorial/creatingcse)
4. Create a directory in your system and move to it
5. Download the raw files using ```wget```:
```
wget https://raw.githubusercontent.com/kytrnd/twitter-image-reply-bot/master/image-reply-bot/img_reply_bot.py
```
```
wget https://raw.githubusercontent.com/kytrnd/twitter-image-reply-bot/master/image-reply-bot/setup.py
```
6. Install Python3:
```
sudo apt-get install python3
```
7. Install Twython and search_google using ```pip3```:

```
pip3 install twython
```
```
pip3 install search_google
```

## Running the script

After completing the previous steps, move the img_reply_bot.py file to your directory.
Change some variables like directories and developer keys.

Execute using Python 3:

```
python3 img_reply_bot.py
```


## Built With
* [Python (3.5.2)](https://docs.python.org/3/)
* [Twython (3.6.0)](https://twython.readthedocs.io/en/latest/index.html)
* [search_google (1.2.0)](https://rrwen.github.io/search_google/)

### Contact Info
* david.ortiz11@upr.edu
