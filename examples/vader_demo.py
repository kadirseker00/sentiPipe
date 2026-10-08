"""Illustrate the English VADER baseline with synthetic review sentences."""
import json

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def main():
    analyzer = SentimentIntensityAnalyzer()
    reviews = [
        "I love this product! It works perfectly.",
        "The item arrived on Tuesday.",
        "This is terrible. I hate it.",
    ]
    results = []
    for text in reviews:
        scores = analyzer.polarity_scores(text)
        compound = scores["compound"]
        label = "positive" if compound >= 0.05 else "negative" if compound <= -0.05 else "neutral"
        results.append({"text": text, "sentiment": label, "scores": scores})
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
