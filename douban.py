# -*- coding: utf-8 -*-
import scrapy
import urllib


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    # start_urls = ['https://accounts.douban.com/login']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}  # 供登录模拟使用

    def start_requests(self):
        login_url = 'https://accounts.douban.com/login'
        yield scrapy.Request(login_url,callback=self.parse)

    def parse(self, response):
        captcha_solution = response.xpath('//img[@id="captcha_image"]/@src').extract()

        # 判断是否存在验证码
        if captcha_solution:
            print '''
                有验证码，准备输入
            '''
            captcha_url = captcha_solution[0]
            print captcha_url
            urllib.urlretrieve(captcha_url, 'douban.jpg')
            captcha_solution = raw_input('请输入验证码,本地查看douban.jpg：')

            # 构造表单数据
            data = {
                'form_email': '1752570559@qq.com',
                'form_password': '1234qwer',
                'captcha-solution': captcha_solution,
            }
            # 自动提取表单post地址
            yield scrapy.FormRequest.from_response(
                response,
                headers=self.header,
                formdata=data,
                callback=self.after_login,
            )

        else:
            print '无验证码，直接登陆'

    def after_login(self, response):
        title = response.xpath('//title/text()').extract()[0]
        print title
        if u'登录' in title:
            print '登陆失败'
        else:
            print '登陆成功'
            print response.body
            '''
            处理登陆以后的业务逻辑
            '''


