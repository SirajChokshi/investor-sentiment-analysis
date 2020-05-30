from newspaper import Article
import feedparser
from datetime import datetime

# Error class that mimics the structure of Article from newspaper
class Error:
    def __init__(self, url):
        self.url = url
        self.title = "\u001b[31;1mError:\u001b[37;1m Failed to download from " + url
        self.author = []
        self.publish_date = 0

# parses article for meta information and returns a hydrated article object
# parameters: url <string>
# returns: Article <object>
def parseArticleFromURL(url):
    article = Article(url)
    try:
        article.download()
        article.parse()
        return article
    except:
        return Error(article.url)

# prints an article or error into the console
# parameters: article <object> (Can be Article or Error)
# returns: void
def printArticle(article):
    print("\u001b[37;1m" + article.title)
    if article.publish_date != 0:
        print("\u001b[0m" + "Written by {} on {}".format(article.authors, (article.publish_date).strftime("%m/%d/%Y")))

# finds and returns a list of articles for a received ticker, verbose mode will print out articles as they are scraped
# parameters: ticket <string>, verbose <boolean>
# returns: article_list <list>
def scrapeArticles(ticker, verbose=False):
    rss_feed = feedparser.parse("https://feeds.finance.yahoo.com/rss/2.0/headline?s={}&region=US&lang=en-US".format(ticker))
    article_list = []
    for entry in rss_feed.entries:
        current_article = parseArticleFromURL(entry.link)
        article_list.append(current_article)
        if verbose:
            printArticle(current_article)
    return article_list