import feedparser

def fetch_google_news_topics():
    feed_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(feed_url)
    articles = [{"title": entry.title, "link": entry.link} for entry in feed.entries]
    return articles
