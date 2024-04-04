import requests
import json
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

auth_request = session.post(
    "https://idfs.gs.com/as/token.oauth2", data=auth_data)
access_token_dict = json.loads(auth_request.text)
print(access_token_dict)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization": "Bearer " + access_token})

request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"

request_query = {
    "where": {
        "gsid": ["75154", "193067", "194688", "902608", "85627"]
    },
    "startDate": "2017-01-15",
    "endDate": "2018-01-15"
}

request = session.post(url=request_url, json=request_query)
results = json.loads(request.text)

print(results)