import requests

from datetime import datetime
from line_notify import line_notify

TOKYO_CODE = 130000


def get_weather(code):

    #３日間(最大)の天気予報を取得
    api_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{code}.json"
    weather_data = requests.get(api_url).json()

    area_name = weather_data[0]["timeSeries"][0]['areas'][0]['area']['name']
    time_series = weather_data[0]["timeSeries"][0]["timeDefines"]
    weather_series = weather_data[0]["timeSeries"][0]["areas"][0]["weathers"]

    weathers = f"{len(time_series)}日間の天気予報\n"
    for time, weather in zip(time_series, weather_series):
        time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S+09:00")  #strptime→文字列をdateime型に変換する。
        weathers += f"\t{time} の {area_name} の天気は{weather} です。\n"
        print(weathers)
    else:
        weathers += "\n"
        #天気予報詳細を取得
        detail_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{code}.json"
        weather_data = requests.get(detail_url).json()
        weathers += weather_data["text"]

        return weathers


weather_info = get_weather(TOKYO_CODE)
print(weather_info)
line_notify(weather_info)
