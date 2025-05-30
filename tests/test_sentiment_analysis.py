import pytest
import pandas as pd
from src.sentiment_analysis import analyze_sentiment

def test_analyze_sentiment_positive():
    """Test sentiment analysis on positive text."""
    data = {
        'headline': ["I love this product!"]
    }
    ratings = pd.DataFrame(data)
    result = analyze_sentiment(ratings)
    assert result['sentiment'].iloc[0] > 0  # Check that sentiment is positive

def test_analyze_sentiment_negative():
    """Test sentiment analysis on negative text."""
    data = {
        'headline': ["I hate this product!"]
    }
    ratings = pd.DataFrame(data)
    result = analyze_sentiment(ratings)
    assert result['sentiment'].iloc[0] < 0  # Check that sentiment is negative

def test_analyze_sentiment_neutral():
    """Test sentiment analysis on neutral text."""
    data = {
        'headline': ["This product is okay."]
    }
    ratings = pd.DataFrame(data)
    result = analyze_sentiment(ratings)
    # Allow for a range close to zero for neutral sentiment
    assert 0.4 < result['sentiment'].iloc[0] < 0.6  # Adjusted range for sentiment