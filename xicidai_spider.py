#coding:utf8
import urllib2,urllib
import re

base_url = 'http://www.xicidaili.com/nn/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

request= urllib2.Request(base_url,headers=headers) #构造请求对象
response = urllib2.urlopen(request)
html = response.read()

td_pattern = re.compile(r'<td>(.*?)</td>')
td_list = td_pattern.findall(html)

ip_pattern = re.compile(r'^(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])$')
ip_list = []
for td_content in td_list:
    res = ip_pattern.search(td_content)
    if res is not None:
        ip = res.group()
        ip_list.append(ip)

for ip in ip_list:
    print ip

