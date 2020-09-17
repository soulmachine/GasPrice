import json

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}


def get_gas_price():
  response = requests.get('https://www.gasnow.org/api/v3/gas/price?utm_source=soulmachine', headers=headers)
  obj = response.json()
  if obj['code'] == 200:
    return obj['data']
  else:
    return None

if __name__ == "__main__":
    data = get_gas_price()
    if data is not None:
      with open("gasprice.json", "a") as f:
        f.write(json.dumps(data) + '\n')
