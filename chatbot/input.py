#input loop - to be used as backup

from dialogflow import *

uid = 101
inp = input(">>")
while(inp != ""):
    msgs = handle_user_message(inp, uid)
    for msg in msgs:
        print(msg)
    inp = input(">>")