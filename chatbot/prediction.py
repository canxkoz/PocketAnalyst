import requests
import json
import random

import os
from dotenv import load_dotenv

# load auth informations
load_dotenv()
grant_type = os.getenv("GRANT_TYPE")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
scope = os.getenv("SCOPE")

# create session instance
session = requests.Session()

auth_data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret":client_secret,
        "scope": scope
    }


# create session instance
session = requests.Session()


def get_gir_score(ticker, date):
    request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"

    request_query = {
        "where": {
            "ticker": [ticker]
        },
        "startDate": date,
        "endDate": date
    }
    print(request_query)

    try:
        request = session.post(url=request_url, json=request_query)
        results = json.loads(request.text)
        if len(results['data']) > 0:
            return results['data'][0]['integratedScore']
        else:
            return 0
    except Exception:
        return 0

def get_coverage():
    request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/coverage?limit=110"
    request = session.get(url=request_url)
    results = json.loads(request.text)["results"]
    request_url = "https://api.marquee.gs.com/v1/assets/data/query"
    req_parameter = {
        "where": {
            "gsid": [entry["gsid"] for entry in results]
        },
        "fields": ["ticker"],
        "limit": 10000
    }
    request = session.post(url=request_url, json=req_parameter)
    result = json.loads(request.text)["results"]

    return set([entry["ticker"] for entry in result])

def get_gs_decision(gir_score):
    if gir_score > 0.5:
        return 1
    else:
        return 0

def get_10_stocks():
    a = list(get_coverage())
    random.shuffle(a)
    return a[0:10]

def getStockRecommendation():

    auth_request = session.post(
        "https://idfs.gs.com/as/token.oauth2", data=auth_data)
    access_token_dict = json.loads(auth_request.text)
    access_token = access_token_dict["access_token"]
    session.headers.update({"Authorization": "Bearer " + access_token})

    largest = 0
    largestTicker = 0
    for entry in get_10_stocks():
        gs = get_gir_score(entry, "2015-11-02")
        print(gs)
        if gs > largest:
            largest = gs
            largestTicker = entry
    return (largestTicker, largest)

def getSellRecommendation(tickers):

    auth_request = session.post(
        "https://idfs.gs.com/as/token.oauth2", data=auth_data)
    access_token_dict = json.loads(auth_request.text)
    access_token = access_token_dict["access_token"]
    session.headers.update({"Authorization": "Bearer " + access_token})

    smallest = 1
    smallestTicker = ""
    for entry in tickers:
        if entry == "USD":
            continue
        gs = get_gir_score(entry, "2015-11-02")
        if gs < smallest:
            smallest = gs
            smallestTicker = entry
    return (smallestTicker, smallest)

from iexfinance.stocks import Stock
IEX_TOKEN = os.getenv("IEX_TOKEN")

def get_beta(ticker):
    stock = Stock(ticker, token=IEX_TOKEN)
    return stock.get_beta()

def volatility_check(ticker):
    if get_beta(ticker) > 1:
        return 0
    else:
        return 1