import datetime
import sys
import time
import telepot
import pprint
from subprocess import *
from telepot.loop import MessageLoop
bot = telepot.Bot("")

def send():
    out = check_output(['sensors'])
    times=str(datetime.datetime.now())
    bot.sendMessage("-1001217797725", out+'\n'+times)
    print("send "+times)


while 1:
    send()
    time.sleep(60*60)

# https://api.telegram.org//getUpdates
# https://api.telegram.org//sendMessage?chat_id=@publicinc&text=helloword

