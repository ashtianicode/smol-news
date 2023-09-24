1. Variables:
   - `TWEET_STREAM`: A socket stream of tweets, used in `main.py`, `twitter_stream.py`.
   - `GPT3_MODEL`: The GPT-3 model used for sentiment analysis, used in `main.py`, `gpt3_sentiment_analysis.py`.
   - `STOCK_LIST`: A list of all stocks and their aliases, used in `main.py`, `stock_list.py`, `backtesting.py`.
   - `REDIS_DB`: The Redis database instance, used in `main.py`, `redis_db.py`.
   - `BACKTEST_DATA`: The 1 year worth of data for backtesting, used in `main.py`, `backtesting.py`.

2. Data Schemas:
   - `Tweet`: The schema for a tweet, used in `twitter_stream.py`, `gpt3_sentiment_analysis.py`.
   - `Stock`: The schema for a stock, used in `stock_list.py`, `redis_db.py`, `backtesting.py`.
   - `Prediction`: The schema for a prediction, used in `gpt3_sentiment_analysis.py`, `redis_db.py`.

3. Function Names:
   - `stream_tweets()`: Function to stream tweets, used in `main.py`, `twitter_stream.py`.
   - `analyze_sentiment()`: Function to analyze sentiment, used in `main.py`, `gpt3_sentiment_analysis.py`.
   - `get_stock_list()`: Function to get the list of stocks, used in `main.py`, `stock_list.py`.
   - `update_redis_db()`: Function to update the Redis database, used in `main.py`, `redis_db.py`.
   - `backtest_strategy()`: Function to backtest the strategy, used in `main.py`, `backtesting.py`.

4. Configurations:
   - `CONFIG`: The configuration object, used in all files.

5. Docker:
   - `DOCKERFILE`: The Dockerfile to set up the environment, used in `dockerfile`.

6. Requirements:
   - `REQUIREMENTS`: The list of Python dependencies, used in `requirements.txt`.

7. CSV Files:
   - `stock_aliases.csv`: CSV file containing stock aliases, used in `stock_list.py`.
   - `one_year_data.csv`: CSV file containing one year worth of data, used in `backtesting.py`.