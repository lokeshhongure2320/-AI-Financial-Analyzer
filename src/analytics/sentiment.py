from textblob import TextBlob

def sentiment_score(texts):
    scores = [TextBlob(t).sentiment.polarity for t in texts]
    return sum(scores) / len(scores)