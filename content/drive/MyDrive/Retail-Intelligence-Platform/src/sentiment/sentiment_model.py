
from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

def analyze_review(text):
    return sentiment(text)[0]

if __name__ == "__main__":
    print(analyze_review("This product is amazing!"))
