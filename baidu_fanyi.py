#coding:utf8
import urllib2
import urllib
import json

def translate(key):
    base_url = 'https://fanyi.baidu.com/v2transapi'

    data = {
        "from": "en",
        "to": "zh",
        "query": key,
        "simple_means_flag": "3",
    }

    data = urllib.urlencode(data)  # data必须urlencode一下
    requeset = urllib2.Request(base_url,data=data)  #发的是post请求，data是urlencode以后的编码
    response = urllib2.urlopen(requeset) #发起请求
    data_json = response.read()  # 读取响应体
    data = json.loads(data_json)  #把json转换成python字典
    # print json.dumps(data,indent=4,ensure_ascii=False) #把python字典友好的格式化输出 接受一个字典对象  indent 缩进空格
    res = data['dict_result']['simple_means']['word_means']  #字典中获取翻译后的内容
    for item in res:
        print item

if __name__ == '__main__':
    while True:
        key = raw_input('输入翻译单词：')
        if key == 'q':
            exit()
        else:
            translate(key)