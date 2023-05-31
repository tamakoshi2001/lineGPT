import requests
import json
from env import chatGPT_api_key, LINE_channel_access_token


def json_dump(reply):
    return reply.get_json(silent=True)


def chatGPT_api(text):
    # Chat GPT APIのエンドポイント
    api_endpoint = "https://api.openai.com/v1/chat/completions"

    # Chat GPT APIの認証情報
    api_key = chatGPT_api_key

    # Chat GPT APIに送信するデータの作成
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": text}],
        "temperature": 0.7
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Chat GPT APIへのリクエストの送信
    response = requests.post(
        api_endpoint, data=json.dumps(payload), headers=headers)

    # レスポンスのJSONを取得
    response_json = response.json()

    # Chat GPTの応答を抽出
    response_from_chatGPT = response_json['choices'][0]['message']['content']

    return response_from_chatGPT


def line_api(reply_token, text):
    api_endpoint = "https://api.line.me/v2/bot/message/reply"

    # LINEチャネルアクセストークン
    channel_access_token = LINE_channel_access_token
    messages = [
        {
            "type": "text",
            "text": text
        }]
    # LINE Messaging APIに送信するデータの作成
    payload = {
        "replyToken": reply_token,
        "messages": messages
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}"
    }

    response = requests.post(
        api_endpoint, data=json.dumps(payload), headers=headers)

    # LINE Messaging APIへのリクエストの送信
    return response.status_code
