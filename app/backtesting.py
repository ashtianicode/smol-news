```python
import pandas as pd
from config import CONFIG
from stock_list import STOCK_LIST

BACKTEST_DATA = pd.read_csv(CONFIG['one_year_data_path'])

def backtest_strategy():
    total_profit = 0
    for stock in STOCK_LIST:
        stock_data = BACKTEST_DATA[BACKTEST_DATA['stock'] == stock]
        for i in range(1, len(stock_data)):
            previous_day = stock_data.iloc[i-1]
            current_day = stock_data.iloc[i]
            if previous_day['prediction'] == 'POSITIVE' and current_day['close'] > previous_day['close']:
                total_profit += current_day['close'] - previous_day['close']
            elif previous_day['prediction'] == 'NEGATIVE' and current_day['close'] < previous_day['close']:
                total_profit += previous_day['close'] - current_day['close']
    return total_profit
```