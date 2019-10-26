'''
flask api to deal with facebook stuff
'''


import random
from flask import Flask, request
from pymessenger.bot import Bot
from pymessenger2.bot import Bot as Bot2

from config import *
from dialogflow import *

app = Flask(__name__)
ACCESS_TOKEN = FB_ACCESS_TOKEN
VERIFY_TOKEN = FB_VERIFY_TOKEN
bot = Bot(ACCESS_TOKEN)
bot2 = Bot2(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if request was not get, we can assume it was POST
    else:
        try:
            print("got a post")
            output = request.get_json()
            for event in output['entry']:
                messaging = event['messaging']
                for message in messaging:
                    if message.get('message'):
                        recipient_id = message['sender']['id'] #Facebook Messenger ID of user
                        received_msg = message['message'].get('text')
                        msgs = handle_user_message(received_msg, recipient_id)
                        if msgs:
                            for msg in msgs:
                                if isinstance(msg, str):
                                    send_message(recipient_id, msg)
                                else:
                                    #it's an image object
                                    send_image(recipient_id, msg["path"])
        except:
            print("error occurred")
            return "msg processed"
    return "msg processed"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def send_image(recipient_id, path):
    bot2.send_image(recipient_id, path)
    return "success"

if __name__ == "__main__":
    app.run()