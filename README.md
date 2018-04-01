# Image Reply Bot

This script obtains user mentions via Twython (3.6.0), a Python wrapper for the Twitter API and replies with 4 query-based png images obtained through the search_google (1.2.0) a module for Google API image search.

## Getting Started

1. Create a Twitter account if you don't already have one.
  1.a. You can use your own personal account, but I believe it's best to use one solely for this project.
2. Create a Twitter application
  2.a. For more info visit: https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/
3. Create your Custom Search Engine with Google
  3.a. For more info visit: https://developers.google.com/custom-search/docs/tutorial/creatingcse
4. This project was developed using Ubuntu for Windows 10, I assume it can be easily recreated for Unix distros and OSX with minor tweaking.

### Prerequisites

Once in your project folder in your terminal install the following:

Python (3.5.2)

```
sudo apt-get install python3
```

Twython (3.6.0)

```
pip3 install twython
```

search_google (1.2.0)

```
pip3 install search_google
```

## Running the script

After completing the previous steps, move the img_reply_bot.1.0.0.py file to your directory.
Change some variables like directories and developer keys.

Execute using Python 3:

```
python3 img_reply_bot.1.0.0.py
```

## Built With

* [Python](https://docs.python.org/3/) - Programming language
* [Twython](https://twython.readthedocs.io/en/latest/index.html) - Python wrapper for Twitter API
* [search_google](https://rrwen.github.io/search_google/) - Python module for Google Custom Search API

## Versioning

I reffered to [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **David J. Ortiz Rivera** - *Initial work* - [kytrnd](https://github.com/kytrnd)

## Acknowledgments

* Family and friends for testing

## Contact Info:

* e-mail: david.ortiz11@upr.edu
