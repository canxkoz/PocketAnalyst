import os
from dotenv import load_dotenv
load_dotenv()

DIALOGFLOW_PROJECT_ID = 'sinuous-axiom-257104'
DIALOGFLOW_LANGUAGE_CODE = 'en-US'
GOOGLE_APPLICATION_CREDENTIALS = 'service-acc-creds.json'

PROTECTED_INTENTS = set([
    "check-balance",
    "deposit-money",
    "buy-stock",
    "sell-stock"
])

FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
FB_VERIFY_TOKEN = os.getenv("FB_VERIFY_TOKEN")


#DOCUSIGN ACCESS TOKEN WILL EXPIRE EVERY EIGHT HOURS - reset it before demo
DOCUSIGN_ACCESS_TOKEN = os.getenv("DOCUSIGN_ACCESS_TOKEN")
DOCUSIGN_ACCOUNT_ID = os.getenv("DOCUSIGN_ACCOUNT_ID")

SLACK_TOKEN = os.getenv("SLACK_TOKEN")

TELEGRAM_BOT_KEY = os.getenv("TELEGRAM_BOT_KEY")