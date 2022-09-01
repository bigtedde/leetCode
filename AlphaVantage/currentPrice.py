import json

import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"function": "GLOBAL_QUOTE", "symbol": "RBLX", "datatype": "json"}

headers = {
    "X-RapidAPI-Key": "0c13cf9ad9msh86efdcbb1400cfbp1b3befjsn902ac8bd10bc",
    "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
y = json.loads(response.text)
print(y)
print(y["Global Quote"])
print(y["Global Quote"]["05. price"])
