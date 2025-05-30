from setuptools import setup, find_packages

setup(
    name='news_sentiment_driven_stock_predictor',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)