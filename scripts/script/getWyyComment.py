import requests
import json
import re
import jieba
import jieba.analyse

# 判断感情的关键词
keyWords = {'爱情', '感情', '喜欢', '分开', '离开', 'love', '再见', '高一', '孩子', '责任', '存在', '得到', '失去', '距离', '记得', '模糊', '暗恋',
            '学校', '城市', '肚子痛', '可爱', '发小', '散伙饭', '同学', '背影', '陌生', '名字', '青春', '新郎', '新娘', '民谣', '告白', '初吻',
            '分手', '声音', '去年', '初三', '高三', '大学', '干净', '年级', '年龄', '电影', '约定', '宿舍', '逝去', '珍惜', '关系', '后悔', '幼稚', '拜拜',
            '再见', '离开', '年轻', '女朋友', '毕业', '遇到', '心碎', '陌生', '害怕', '遗憾', '長大', '公主', '王子', '晚上', '凌晨', '眼神', '中年', '想起', '失眠', '噩梦',
            '微风', '欢喜'}


# 歌曲获取循环
def getWyyComment():
    for songId in [1827600686, 1394963332, 167873]:
        # 获取歌曲评论循环
        for page in range(1, 10000):
            print(f'开始获取第{page}页数据')
            endList = []
            url = f"http://localhost:3000/comment/new?type=0&id={songId}&sortType=1&pageNo={page}"
            response = requests.get(url)
            data = json.loads(response.text)['data']['comments']
            # 判断当前页面是否存在数据，没有数据跳出这个首歌
            if not data:
                break
            else:
                for item in data:
                    # 歌词关键词分割
                    dataList = jieba.analyse.extract_tags(item['content'], topK=20, withWeight=False,
                                                          allowPOS=(
                                                              'ns', 'n', 'vn', 'v', 'TIME', 'LOC', 'PER', 'a', 'b',
                                                              't'))
                    # 判断分割的关键词中是否包含有上面关于感情的关键词
                    if set(dataList) & keyWords:
                        for keyWord in dataList:
                            endList.append(keyWord)
                # 数据写入到文本中
                print('开始写入数据')
                with open('data/wyyComment.txt', 'a+') as fp:
                    for i in endList:
                        fp.write(i + ',')
                print('数据写入完成')
                print('数据获取完成')
                print(f'第{page}页获取数据长度为', len(endList))
