import os
import requests

from dotenv import load_dotenv


def line_notify(message):
    """
    :param message:
    :return:
    LINE Notify APIを使用してメッセージを送信
        最後は自分のAPIを取得するようにするとプログラムの中でheaderから処理が実行され自分のLINEにプログラムが実行される。"""

    load_dotenv()
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {os.getenv("LINE_TOKEN")}'}
    payload = {'message': message}
    responce = requests.post(line_notify_api, headers=headers, data=payload)
    print(responce.status_code)

