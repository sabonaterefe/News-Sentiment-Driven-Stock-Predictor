from textblob import TextBlob
import pandas as pd

def analyze_sentiment(ratings: pd.DataFrame) -> pd.DataFrame:
    """Perform sentiment analysis on headlines"""
    # Basic sentiment
    ratings['sentiment'] = ratings['headline'].apply(
        lambda x: TextBlob(x).sentiment.polarity
    )
    
    # Enhanced sentiment with keyword weighting
    def enhanced_sentiment(text):
        blob = TextBlob(text)
        negative_words = {'cut', 'lower', 'reduce', 'sell', 'bearish'}
        positive_words = {'raise', 'increase', 'buy', 'bullish', 'upgrade'}
        
        words = set(text.lower().split())
        if words & negative_words:
            return blob.sentiment.polarity * 1.5
        elif words & positive_words:
            return blob.sentiment.polarity * 1.2
        return blob.sentiment.polarity
    
    ratings['enhanced_sentiment'] = ratings['headline'].apply(enhanced_sentiment)
    return ratings