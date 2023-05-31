# lineGPT

某チャットくんの自作です。GCP、chatGPT API、Messaging APIをつかって作成しました。

# DEMO
<img src="https://github.com/tamakoshi2001/lineGPT/assets/72233550/a416fa20-770a-4732-9268-f801412942cc" width="300px">\
# Usage
前準備\
1.chatGPT APIと、Line botのchannel access tokenを取得して、env.pyを作成し、chatGPT_api_key, LINE_channel_access_tokenという変数にそれぞれ入力してください。\
\
cloud Functions\
2.GCPのcloud Functionにファイルをアップロードしてください。\
3.cloud FunctionsにallUserの起動元権限追加。cloud RUNに未認証の呼び出し許可をしてください。\
\
LINE\
4.Message APIのWebhook URLにcloud FunctionのトリガーURLを入力してください。\
5.Line botでchatGPTが使えるようになります。botのメッセージ設定を調整してお楽しみください。

# Author

* 作成者 Yuji Tamakoshi
* E-mail　uotstudent2001@g.ecc.u-tokyo.ac.jp
