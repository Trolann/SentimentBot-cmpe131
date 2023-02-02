import nltk
from nltk.corpus import words
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def determine_sentiment(word):
    sentiment = SentimentIntensityAnalyzer().polarity_scores(word)
    if sentiment["compound"] > 0.05:
        return "Positive"
    elif sentiment["compound"] < -0.05:
        return "Negative"
    else:
        return "Neutral"

def main(text):
    is_word = text.strip().lower() in words.words()
    if not is_word:
        raise ValueError("Not a valid English word")
    else:
        sentiment = determine_sentiment(text)
        print(f"Sentiment of the word is: {sentiment}")

if __name__ == "__main__":
    nltk.download("vader_lexicon")
    nltk.download("words")
    while True:
	    text = input("Enter a text string: ")
	    try:
	      main(text)
	    except:
	      continue
			