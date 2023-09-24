```python
import json
import csv
from datetime import datetime

def load_config():
    with open('app/config.py', 'r') as file:
        CONFIG = json.load(file)
    return CONFIG

def load_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def parse_tweet(tweet):
    tweet_data = json.loads(tweet)
    return tweet_data

def format_prediction(prediction):
    formatted_prediction = {
        "sentiment": prediction['choices'][0]['text'].strip(),
        "magnitude": prediction['choices'][0]['finish_reason']
    }
    return formatted_prediction

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```