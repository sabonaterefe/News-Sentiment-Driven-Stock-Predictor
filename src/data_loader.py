import os
import pandas as pd
from typing import Dict, Tuple

def clean_ratings(ratings: pd.DataFrame) -> pd.DataFrame:
    """Clean the analyst ratings data."""
    ratings['date'] = pd.to_datetime(ratings['date'], utc=True, errors='coerce')
    ratings.dropna(subset=['date'], inplace=True)  # Drop rows where date is missing
    ratings.drop_duplicates(inplace=True)
    return ratings

def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean individual stock data."""
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date', 'Close'], inplace=True)  # Ensure necessary columns are not missing
    df['Daily_Return'] = df['Close'].pct_change()  # Calculate daily returns
    df.set_index('Date', inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def load_all_data() -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]:
    """Load and clean all data files."""
    # Load analyst ratings
    ratings = pd.read_csv('../data/raw_analyst_ratings/raw_analyst_ratings.csv')
    ratings = clean_ratings(ratings)

    # Load stock data
    stocks = {}
    for file in os.listdir('../data/yfinance_data'):
        if file.endswith('_historical_data.csv'):
            ticker = file.split('_')[0]
            df = pd.read_csv(f'../data/yfinance_data/{file}')
            df = clean_stock_data(df)
            stocks[ticker] = df
            
    return ratings, stocks


ratings, stocks = load_all_data()

# Accessing daily returns for a specific stock, e.g., 'AAPL'
ticker = 'AAPL'
if ticker in stocks:
    daily_returns = stocks[ticker]['Daily_Return']
    print(daily_returns.head())
else:
    print(f"{ticker} data not found.")