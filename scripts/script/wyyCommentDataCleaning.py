import json
import os


# 删除原本文件
def delFile():
    try:
        os.remove('../../src/data/data.json')
    except OSError:
        pass


def wyyCommentCleaning():
    delFile()
    wyyCommentJsonData = dict()
    wyyCommentListData = []
    wyyCommentListDataEnd = []
    with open('data/wyyComment.txt', 'r') as fp:
        data = fp.read()
        dataList = data.split(',')
        dataSet = set(dataList)
        for keyWord in dataSet:
            if keyWord == '':
                continue
            value = dataList.count(keyWord)
            wyyCommentListData.append({'name': keyWord, 'value': value})

    wyyCommentListDataEnd = [item for item in wyyCommentListData if item['value'] > 5]
    wyyCommentJsonData = {'data': wyyCommentListDataEnd}
    with open('../src/data/data.json', 'w+', encoding='utf8') as fp:
        json.dump(wyyCommentJsonData, fp, ensure_ascii=False)
