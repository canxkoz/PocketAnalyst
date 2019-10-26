import requests

def nameToTicker(name):
    res = requests.get("http://d.yimg.com/autoc.finance.yahoo.com/autoc?query="+name+"&region=1&lang=en")
    return res.json()["ResultSet"]["Result"][0]["symbol"]