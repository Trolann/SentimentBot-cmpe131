import unittest
from main import determine_sentiment, main

class TestSentiment(unittest.TestCase):
    def test_positive_sentiment(self):
        word = "love"
        sentiment = determine_sentiment(word)
        self.assertEqual(sentiment, "Positive")

    def test_negative_sentiment(self):
        word = "hate"
        sentiment = determine_sentiment(word)
        self.assertEqual(sentiment, "Negative")

    def test_neutral_sentiment(self):
        word = "neutral"
        sentiment = determine_sentiment(word)
        self.assertEqual(sentiment, "Neutral")