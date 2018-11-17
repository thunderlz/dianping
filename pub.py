# 爬虫公共类
# -*- coding: utf-8 -*-
# code by leiz

import requests

class pachong():
    def __init__(self,host):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
            , 'Accept-Language': 'zh-CN,zh;q=0.9'
            , 'Accept-Encoding': 'gzip, deflate'
            # ,'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            ,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
            , 'Host': host
            , 'Connection': 'keep-alive'
            , 'Cache-Control': 'max-age=0'
            , 'Upgrade-Insecure-Requests': '1'}

    def getHtml(self,url, params=''):
        s = requests.Session()
        for i in range(3):
            try:
                resp = s.get(url, headers=self.headers, params=params, timeout=10)
                if resp.status_code == 200:
                    return resp.content
                else:
                    print(resp.status_code)
                    return None
            except:
                print('timeout for {}'.format(i + 1))
            return  None

if __name__=='__main__':

    p=pachong('www.baidu.com')
    print(p.headers)