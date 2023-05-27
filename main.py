from modules import *
import functions_framework


@functions_framework.http
def main(request):
    try:
        reply = json_dump(request)

        # Webhook verify
        if reply['events'] == []:
            return ({}, 200)

        text = reply['events'][0]['message']['text']
        reply_token = reply['events'][0]['replyToken']
        # chatGPTからの受信
        completions = chatGPT_api(text)
        # LINEbotに送信
        status_code = line_api(reply_token, completions)

        if status_code == 200:
            print("Message replied successfully.")
        else:
            print(f"Message reply failed with status code: {status_code}")
        return '200'
    except Exception as e:
        print(str(e))
        return '500'
