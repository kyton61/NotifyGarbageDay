#!/usr/bin/env python
# encoding: utf-8

#import boto3
import calendar
import datetime
#import requests
import os
import locale
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

# LINEの設定
#LINEPOSTURL = os.environ['LINEPostURL']
#LINETOKEN = os.environ['LINEtoken']
#headers = {"Authorization" : "Bearer "+ LINETOKEN}

def get_day_of_week_jp(weekday):
    w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return(w_list[weekday])

def get_number_of_weekday(dt):
    # 今日の日付から7日引いていき、第何週目(weeks)かを調べる
    day = dt.day
    weeks = 0
    while day > 0:
        weeks += 1
        day -= 7

    return weeks

def get_garbageday(dt,weekday):
    # 今日の日時、明日の曜日から何のごみの日かを決める
    if weekday == "火曜日":
        text = "資源ごみ"
    elif weekday == "水曜日" or weekday == "土曜日":
        text = "可燃ごみ"
    elif weekday == "木曜日":
        # 第2 or 第4 木曜日かどうか判定
        num = get_nubmer_of_weekday(dt)
        if num == 2 or num == 4:
            text = "不燃ごみ"
        else:
            print("不燃ごみの木曜日だが、第2、第4週目ではないためスキップ")
            exit(0)
    else:
        test = "明日はごみの日ではありません（例外エラー発生！汗）"
        
    return text

def build_message(weekday,garbageday):
    text = "明日%sは%sの日です。8時までに出してください。" % (weekday,garbageday)
    return text

def main():
    # 現在日時のdatetimeオブジェクトを取得
    dt = datetime.datetime.now()
    # 今日の曜日を取得
    #day = get_day_of_week_jp(dt.weekday())
    #print(day)
    # 明日の曜日を取得
    weekday = get_day_of_week_jp(dt.weekday() + 1)
    print(weekday)
    # なんのごみの日かを取得
    garbageday = get_garbageday(dt,weekday)

    message = build_message(weekday,garbageday)

    print(message)

    #payload = {"message" : message}
    #try :
    #    req = requests.post(LINEPOSTURL,headers = headers, params=payload)
    #except requests.exceptions.RequestException as e:
    #    logger.error("Requests failed: %s", e)

main()
