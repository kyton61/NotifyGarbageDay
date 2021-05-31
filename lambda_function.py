#!/usr/bin/env python
# encoding: utf-8

#import boto3
import datetime
import requests
import os
import locale
import logging

logger = logging.getLogger()
logger.setLevel(loggint.INFO)
locale.setlocation(locale.LC_TIME, 'ja_JP.UTF-8')

# LINEの設定
#LINEPOSTURL = os.environ['LINEPostURL']
#LINETOKEN = os.environ['LINEtoken']
#headers = {"Authorization" : "Bearer "+ LINETOKEN}

def get_garbageday(dt,day)
    # 今の日時から何のごみの日かを決める
    # 曜日の確認
    if day == "月曜日"
        test = "資源ごみ"
    else if day == "火曜日" or "金曜日"
        test = "可燃ごみ"
    else if day == "水曜日"
        if dt
        


    return text

def build_message(day,garbageday)
    test = "明日$sは%sの日です。8時までに出してください。" % (day,garbageday)
    return text

def lambda_handler(event, context):
    # 現在日時のdatetimeオブジェクトを取得
    dt = datetime.datetime.now()
    # 曜日を取得
    day = dt.strftime('%A')
    print(day)
    # なんのごみの日かを取得
    garbageday = get_garbageday(dt)

    message = build_message(day,garbageday)
    payload = {"message" : message}
    try :
        req = requests.post(LINEPOSTURL,headers = headers, params=payload)
    except requests.exceptions.RequestException as e:
        logger.error("Requests failed: %s", e)
