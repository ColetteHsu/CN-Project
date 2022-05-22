from ast import If
import os
import json
from crawler import *
from parser import *
from starbug import *
from linebot.models import *
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *



app = Flask(__name__)

Channel_Access_Token = os.environ.get('Channel_Access_Token')
line_bot_api    = LineBotApi(Channel_Access_Token)
Channel_Secret  = os.environ.get('Channel_Secret')
handler = WebhookHandler(Channel_Secret)

# handle request from "/callback" 
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body      = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# handle text message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    
    if "美食" in msg:
        result=food()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"哪些新聞"in msg:
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = '請選擇新聞類型',
                contents = json.load(open('news.json', 'r', encoding='utf-8'))
            )
        )
    elif"即時"in msg:
        result=today()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"娛樂"in msg:
        result=entertainment()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"運動"in msg:
        result=sport()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )    
    elif"生活"in msg:
        result=life()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"國際"in msg:
        result=internet()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"疫情"in msg:
        result=covidnews()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"電影"in msg:
        result=movie()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"科技"in msg:
        result=it()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"時尚"in msg:
        result=fashion()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"星座"in msg:
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text = '本日星座運勢',
                contents = json.load(open('star.json', 'r', encoding='utf-8'))
            )
        )
    elif"唐老師"in msg:
        result = star(msg)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result)
        )
    elif"今日確診人數"in msg:
        reply_arr=[]
        imgcovid="https://images.jifo.co/1473482_1653113223268.jpg"
        message = ImageSendMessage(
            original_content_url = imgcovid,
            preview_image_url    = imgcovid
            )
        result=covid()
        reply_arr.append(TextSendMessage(text=result))
        reply_arr.append(message)
        line_bot_api.reply_message(event.reply_token, reply_arr)
    else:
        result=others()
        reply_arr=[]
        reply_arr.append(TextSendMessage(text="請輸入”美食 運動 娛樂 即時 星座 國際 生活 疫情 電影 時尚 科技“以提供相關新聞!"))
        reply_arr.append(TextSendMessage(text="幫您查詢相關新聞："+result+msg))
        line_bot_api.reply_message(
            event.reply_token, reply_arr)
            #TextSendMessage(text=msg)
        

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
