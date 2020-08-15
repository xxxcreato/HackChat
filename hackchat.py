#!/usr/bin/env python
# -- coding: utf-8 --

import json
import websocket
import threading
import random
import os
import time
os.system("figlet HACK CHAT")
oda = input("Enter room ID:")
print("Url:https://hack.chat/?{}".format(oda))
ws=websocket.create_connection("wss://hack.chat/chat-ws")
print("[+] Connection OK")
nick=input("Enter Nickname: ")
ws.send(json.dumps({"cmd":"join","channel":"{}".format(oda),"nick":nick}))
def onliness(wait):
	time.sleep(wait)
	onlines=json.loads(ws.recv())["nicks"]
	print("Online Users: "+', '.join(onlines))
onliness(0)
def recvThread():
    while 1:
        data=json.loads(ws.recv())
        if(data["cmd"]=="chat"):
            if(data["nick"]!=nick):
                print("\n"+data["nick"]+":"+data["text"])
        print("\r{}:".format(nick)+str(),end="")
threading.Thread(target=recvThread).start()
while 1:
    print("\r{}:".format(nick)+str(),end="")
    data=input("")
    data={"cmd":"chat","text":"\n"+data+"\n"}
    ws.send(json.dumps(data))
