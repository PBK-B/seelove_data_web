import requests
import json
import random
from getWyyHotPlayList import selectWyyHostPlayList


# 随机获取一个热门歌单id
def selectWyyHostPlayListId():
    hostPlayList = selectWyyHostPlayList()
    playListId = random.choice(list(hostPlayList))
    return playListId


# 获取热门个歌单里面所有歌曲的id
def selectWyyHostPlayListInfo():
    id = selectWyyHostPlayListId()
    url = f'http://localhost:3000/playlist/detail?id={id}'
    response = requests.get(url)
    data = json.loads(response.text)
    if data['code'] == 200:
        print(url)
        print(data)
        for i in data['privileges']:
            yield i['id']
    if data['code'] != 200 or data['privileges'] is None:
        selectWyyHostPlayListId()
        selectWyyHostPlayListInfo()

