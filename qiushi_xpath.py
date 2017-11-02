from lxml import etree
import requests
import json

base_url = 'https://www.qiushibaike.com/hot/page/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
}

with open('duanzi.json','a') as f:
    for i in range(1,2):
        fullurl = base_url + str(i) + '/'
        response = requests.get(fullurl,headers=headers)
        html = etree.HTML(response.content)
        duanzi_div = html.xpath('//div[@id="content-left"]/div')
        for duanzi in duanzi_div:
            nick = duanzi.xpath('.//h2')[0].text.replace('\n','')
            age = duanzi.xpath('.//div[@class="articleGender womenIcon"] | .//div[@class="articleGender manIcon"]')
            if age :
                age = age[0].text

            content = duanzi.xpath('.//div[@class="content"]/span[1]')[0].text.replace('\n','')

            img = duanzi.xpath('.//div[@class="thumb"]//img/@src')

            gaoxiao_num = duanzi.xpath('.//span[@class="stats-vote"]//i[@class="number"]')[0].text

            common_num = duanzi.xpath('.//span[@class="stats-comments"]//i[@class="number"]')[0].text

            item = {
                'nick' : nick,
                'age' : age,
                'content' : content,
                'img' : img,
                'gaoxiao_num' : gaoxiao_num,
                'common_num' : common_num,
            }


            f.write(json.dumps(item,ensure_ascii=False).encode('utf-8') + '\n')


    # for i in range(25):
    #     item = {}
    #
    #     item['nick'] = nick[i]
    #     item['age'] = age[i]
    #
    #
