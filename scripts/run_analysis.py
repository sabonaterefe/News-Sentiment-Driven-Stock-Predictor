from src.data_loader import load_all_data
from src.technical_analysis import calculate_technical_indicators
from src.sentiment_analysis import analyze_sentiment
import os
import pandas as pd

def run_full_analysis():
    # Create results directory
    os.makedirs('results', exist_ok=True)
    
    # Task 1: Load data
    print("Loading data...")
    ratings, stocks = load_all_data()
    
    # Task 2: Technical analysis
    print("Calculating technical indicators...")
    stocks = calculate_technical_indicators(stocks)
    
    # Task 3: Sentiment analysis
    print("Analyzing sentiment...")
    ratings = analyze_sentiment(ratings)
    
    # Save processed data
    print("Saving results...")
    ratings.to_csv('results/processed_ratings.csv', index=False)
    for ticker, data in stocks.items():
        data.to_csv(f'results/{ticker}_processed.csv')
    
    print("Analysis complete! Results saved in /results directory")

if __name__ == "__main__":
    run_full_analysis()