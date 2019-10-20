# Twitter Image Reply Bot

Reply with a query-based album when bot is called. Twitter streaming and api calls are handled using Twython, image scrapping with Google Images Search.

## Getting Started

1. [Create a Twitter account](https://twitter.com/i/flow/signup)
2. [Create a Twitter application](https://developer.twitter.com/en/account/get-started)
3. [Create a Google Custom Search Engine](https://developers.google.com/custom-search/docs/tutorial/creatingcse)
4. Visit [cse](https://cse.google.com/cse/all) and enable "Image search" option and on the "Sites to search" option select "Search the entire web but emphasize included sites".
5. Clone repository:
```
git clone https://github.com/david-SPLTJW/twitter-image-reply-bot.git
cd twitter-image-reply-bot/twitter-image-reply-bot
```
6. Install Python3, Twython and Google Images Search:
```
sudo apt-get install python3
```
```
pip3 install twython
```
```
pip3 install Google-Images-Search
```
7. Set handle and authorization keys in ```setup.py```:
### Filter handle
```
handle = ""
```
### Twitter API keys
```
api_key = ""
api_secret = ""
oauth_token = ""
oauth_token_secret = ""
```
### Google Custom Search API keys
```
cx = ""
google_api_key = ""
```

## Running the script
Execute using Python 3:
```
python3 twitter-image-reply-bot.py
```
Exit by pressing enter

## Built With
* [Python (3.7.4)](https://docs.python.org/3/)
* [Twython (3.7.0)](https://twython.readthedocs.io/en/latest/)
* [Google Images Search (1.0.1)](https://pypi.org/project/Google-Images-Search/)

### Contact Info
* david.ortiz11@upr.edu
