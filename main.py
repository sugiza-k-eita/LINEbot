import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open("infomation.json","r")
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info["CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
#インスタンス化

def main():
    USER_ID = info["USER_ID"]
    #どのuserに送るか
    messagess = TextSendMessage(text="メッセージ内容 \n メッs－じ内容")
    #どのメッセージを送るか
    line_bot_api.push_message(USER_ID, messages=messagess)
    #実際のメソッド
    
if __name__ == "__main__":
    main()
#pythonファイルで実行することを想定している。
#このファイルがメインファイルであれば実行する。