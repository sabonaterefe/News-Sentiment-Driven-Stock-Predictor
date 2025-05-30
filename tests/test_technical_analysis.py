import pytest
import pandas as pd
from src.technical_analysis import calculate_technical_indicators

def test_calculate_technical_indicators():
    """Test calculation of technical indicators."""
    # Sample stock data
    data = {
        'Close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    df = pd.DataFrame(data)
    stocks = {'AAPL': df}

    result = calculate_technical_indicators(stocks)

    # Check that the result contains the calculated indicators
    assert 'MA_20' in result['AAPL'].columns
    assert 'MA_50' in result['AAPL'].columns
    assert 'RSI_14' in result['AAPL'].columns
    assert 'MACD' in result['AAPL'].columns
    assert 'Daily_Return' in result['AAPL'].columns

    # Check some values (you may need to adjust based on your expected results)
    assert result['AAPL']['MA_20'].iloc[-1] is not None
    assert result['AAPL']['RSI_14'].iloc[-1] is not None