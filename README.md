# lineGPT

某チャットくんの自作です。GCP、chatGPT API、Messaging APIをつかって作成しました。

# DEMO
![demo](https://github.com/tamakoshi2001/lineGPT/assets/72233550/a416fa20-770a-4732-9268-f801412942cc)

# Usage
前準備
1.chatGPT APIと、Line botのchannel access tokenを取得して、XXXXに入力してください。

cloud Functions
2.GCPのcloud Functionにファイルをアップロードしてください。
3.cloud FunctionsにallUserの起動元権限追加。cloud RUNに未認証の呼び出し許可をしてください。

LINE
4.Message APIのWebhook URLにcloud FunctionのトリガーURLを入力してください。
5.Line botでchatGPTが使えるようになります。botのメッセージ設定を調整してお楽しみください。

# Note

Message APIでcloud FunctionのWebhook URLをテストする機能がありますが、必ずエラーを起こすので、実機でテストしてください。

# Author

* 作成者 玉腰　勇司
* 所属　東京大学物理工学科4年
* E-mail　uotstudent2001@g.ecc.u-tokyo.ac.jp
