import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def openweathermap_main():
    lat = os.getenv("LAT")
    lon = os.getenv("LON")

    endpoint_url = "https://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&appid={2}&units=metric"
    url = endpoint_url.format(lat, lon, os.getenv('OPENWEATHERMAP_TOKEN'))

    r = requests.get(url)

    response = r.content.decode('utf-8')
    response_json = json.loads(response)

    pass


def mastodon_main():
    endpoint_url = "https://mastodon.social/api/v1/timelines/tag/{0}"
    params = {
        'limit': 40
    }

    headers = {
        "Bearer": os.getenv("ACCESS_TOKEN")
    }

    for i in range(300):
        hashtag = f"day{i}"
        url = endpoint_url.format(hashtag)
        r = requests.get(url, params=params, headers=headers)
        print(f'{i=}')
        r_content = r.content.decode('utf-8')

        r_content_json = json.loads(r_content)

        r_headers = dict(r.headers)
        print(f'{r_headers["x-ratelimit-remaining"]=}')


if __name__ == '__main__':
    openweathermap_main()
    mastodon_main()
