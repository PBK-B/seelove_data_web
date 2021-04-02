import requests
import json


def selectWyyHostPlayList():
    url = 'http://localhost:3000/playlist/hot'
    response = json.loads(requests.get(url).text)
    for i in response['tags']:
        yield i['playlistTag']['id']

    