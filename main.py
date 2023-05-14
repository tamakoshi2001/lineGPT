from modules import *
import functions_framework


@functions_framework.http
def main(request):
    reply = json_dump(request)
    text = reply['events'][0]['message']['text']
    reply_token = reply['events'][0]['replyToken']
    # chatGPTからの返信
    completions = chatGPT_api(text)
    # LINEbotに返信
    status_code = line_api(reply_token, completions)

    if status_code == 200:
        print("Message replied successfully.")
    else:
        print(f"Message reply failed with status code: {status_code}")
    return None


chatGPT_api('who are you?')
