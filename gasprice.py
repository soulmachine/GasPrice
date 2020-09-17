import json
import os
import time
from datetime import datetime, timezone

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}


def get_gas_price():
  response = requests.get('https://www.gasnow.org/api/v3/gas/price?utm_source=soulmachine', headers=headers)
  obj = response.json()
  if obj['code'] == 200:
    with open(os.path.join('data', datetime.now(timezone.utc).strftime("%Y-%m") + ".json"), "a") as f:
      f.write(json.dumps(obj['data']) + '\n')

if __name__ == "__main__":
    for i in range(5): # Run for 5 minutes
      get_gas_price()
      time.sleep(60) # sleep for 60 seconds
