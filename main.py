from textblob import TextBlob

def determine_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main(text):
    sentiment = determine_sentiment(text)
    print(f"Sentiment of the word is: {sentiment}")

if __name__ == "__main__":
    while True:
	    text = input("Enter a text string: ")
	    try:
	      main(text)
	    except:
	      continue
			