import pandas as pd
import numpy as np
from typing import Dict

def calculate_technical_indicators(stocks: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    """Calculate all technical indicators without TA-Lib"""
    for ticker, data in stocks.items():
        # Moving Averages
        data['MA_20'] = data['Close'].rolling(window=20).mean()
        data['MA_50'] = data['Close'].rolling(window=50).mean()
        
        # RSI
        delta = data['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss
        data['RSI_14'] = 100 - (100 / (1 + rs))
        
        # MACD
        ema12 = data['Close'].ewm(span=12, adjust=False).mean()
        ema26 = data['Close'].ewm(span=26, adjust=False).mean()
        data['MACD'] = ema12 - ema26
        data['MACD_Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()
        
        # Daily Returns
        data['Daily_Return'] = data['Close'].pct_change()
        
    return stocks