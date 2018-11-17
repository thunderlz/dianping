import pub
from bs4 import BeautifulSoup
import html5lib
import re
import time
import random

gzfoodP=pub.pachong('www.dianping.com')

numdict={'aq-fjnF':'6', 'aq-cdaf':'0', 'aq-jl2V':'7', 'aq-lQsz':'3', 'aq-fxPw':'9', 'aq-lS9h':'8', 'aq-9dfE':'4', 'aq-iB0b':'5', 'aq-NWJt':'2'}

if __name__ == '__main__':
    with open('f.txt','wt') as f:
        code = set()
        for i in range(1,3):
            time.sleep(random.randint(1,3))
            gzfood=gzfoodP.getHtml('http://www.dianping.com/guangzhou/ch10/g1338p{}'.format(i))
            bsObj=BeautifulSoup(gzfood,'html5lib')
            shops=bsObj.find('div',{'id':'shop-all-list'}).find_all('li')
            for shop in shops:
                print(shop.find('a',{'class':'mean-price'}).get_text())

            # for link in bsObj.findAll('a',{'href':re.compile('http://.*/shop/[0-9]+')}):
            #     if link!=None:
            #         try:
            #             print(link['href'])
            #         except:
            #             print('没有链接')
            #     else:
            #         print(link)

        #     aq=bsObj.find('div',{'id':'shop-all-list'}).find_all('span',{'class':re.compile('aq-.*')})
        #     for li in aq:
        #         # print(li,file=f)
        #         code.add(li['class'][0])
        #         print(li['class'])
        #         # f.flush()
        # print(code)
