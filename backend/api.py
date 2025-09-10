from fastapi import FastAPI
from backend.scraper import fetch_google_news_topics
from backend.summarizer import summarize_articles

app = FastAPI()

@app.get("/topics")
def get_topics():
    articles = fetch_google_news_topics()
    summary = summarize_articles(articles)
    return {"summary": summary, "articles": articles}
