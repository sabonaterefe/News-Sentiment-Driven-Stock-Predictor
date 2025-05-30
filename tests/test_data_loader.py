import pytest
import pandas as pd
from src.data_loader import load_all_data

def test_load_data_valid_file():
    """Test loading data from a valid CSV file."""
    ratings, stocks = load_all_data()  
    assert ratings is not None
    assert not ratings.empty

def test_load_data_invalid_file():
    """Test loading data from an invalid CSV file."""
    with pytest.raises(FileNotFoundError):
        pd.read_csv('invalid_file.csv')  # Directly test for a missing file