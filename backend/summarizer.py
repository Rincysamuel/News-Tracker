from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_articles(articles):
    combined_text = " ".join(article["title"] for article in articles)
    if len(combined_text) > 1024:
        combined_text = combined_text[:1024]
    summary = summarizer(combined_text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
    return summary
