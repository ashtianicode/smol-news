import os

class Config:
    # Twitter API
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    # OpenAI API
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # Redis DB
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

    # Backtesting
    BACKTESTING_DATA_PATH = "data/one_year_data.csv"

    # Stock aliases
    STOCK_ALIASES_PATH = "data/stock_aliases.csv"

    # Socket
    SOCKET_HOST = os.getenv("SOCKET_HOST", "localhost")
    SOCKET_PORT = int(os.getenv("SOCKET_PORT", 9000))