import redis
from config import CONFIG

REDIS_DB = redis.Redis(host=CONFIG['REDIS_HOST'], port=CONFIG['REDIS_PORT'], db=CONFIG['REDIS_DB'])

def update_redis_db(stock, prediction):
    """
    Function to update the Redis database with the prediction for a stock.
    """
    REDIS_DB.set(stock, prediction)

def get_prediction(stock):
    """
    Function to get the prediction for a stock from the Redis database.
    """
    return REDIS_DB.get(stock)

def clear_db():
    """
    Function to clear the Redis database.
    """
    REDIS_DB.flushdb()