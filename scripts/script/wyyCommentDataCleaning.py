import json


def wyyCommentCleaning():
    wyyCommentJsonData = dict()
    wyyCommentListData = []
    with open('data/wyyComment.txt', 'r') as fp:
        data = fp.read()
        dataList = data.split(',')
        dataSet = set(dataList)
        for keyWord in dataSet:
            if keyWord == '':
                continue
            value = dataList.count(keyWord)
            wyyCommentListData.append({'keyWord': keyWord, 'value': value})

    wyyCommentJsonData = {'data': wyyCommentListData}
    with open('../data/wyyCommentJsonData.json', 'w+', encoding='utf8') as fp:
        json.dump(wyyCommentJsonData, fp, ensure_ascii=False)
