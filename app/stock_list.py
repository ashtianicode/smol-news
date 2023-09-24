```python
import csv
import os
from typing import Dict, List

from app.config import CONFIG

STOCK_LIST: Dict[str, List[str]] = {}

def load_stock_aliases() -> Dict[str, List[str]]:
    with open(os.path.join(CONFIG['data_dir'], 'stock_aliases.csv'), 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        for row in reader:
            stock, aliases = row[0], row[1:]
            STOCK_LIST[stock] = aliases
    return STOCK_LIST

def get_stock_list() -> Dict[str, List[str]]:
    if not STOCK_LIST:
        load_stock_aliases()
    return STOCK_LIST
```