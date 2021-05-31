# NotifyGarbageDay
 This is a LINE bot that notifies you of garbage day in Ota ward.

 大田区のごみの日を前日22時にLINE通知するAWS Lambda関数です。

## 起動時刻と通知メッセージ
- 月曜日　22時　明日火曜日は資源ごみの日です。8時までに出してください。
- 火曜日　22時　明日水曜日は可燃ごみの日です。8時までに出してください。
- 金曜日　22時　明日土曜日は可燃ごみの日です。8時までに出してください。
- 第2水曜日　22時　明日第2木曜日は不燃ごみの日です。8時までに出してください。
- 第4水曜日　22時　明日第4木曜日は不燃ごみの日です。8時までに出してください。

## How to use
- AWS Lambda関数にlambda_function.pyをコピー
	ランタイム：python3系
	環境変数：
	- LINEPostURL:https://notify-api.line.me/api/notify(line notifyのURLを指定)
	- LINEtoken: (line notifyのアクセストークンを指定)
- AWS Lambda LayerにLayer.zip（中身はrequestsライブラリ）をアップロード
- トリガーにはEventBridgeを設定
　スケジュール式：cron(0 13 ? * MON,TUE,WED,FRI *)
- test.pyはpython3実行環境でコードテストに使う
	`python test.py`


