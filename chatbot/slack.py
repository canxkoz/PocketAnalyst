from config import *
from dialogflow import *

import os
import slack


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    print(data)
    if data['channel'] == "#pocketanalyst":
        #do stuff

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",
            thread_ts=thread_ts
        )

rtm_client = slack.RTMClient(token=SLACK_TOKEN)
rtm_client.start()