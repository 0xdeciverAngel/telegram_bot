
import datetime
import sys
import time
import telepot
from telepot.loop import MessageLoop
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id,msg)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text']+'\n'+str(datetime.datetime.now()))
    if msg['text']=="/img":                    	
        bot.sendPhoto(chat_id, photo=open("/home/u/camera-live-streaming/live_pic.jpg",'rb'))


bot = telepot.Bot("")
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)
