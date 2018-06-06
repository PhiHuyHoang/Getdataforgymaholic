# -*- coding: utf8 -*-
import sys
import codecs
import sys
import json, requests, bs4 ,os

myfile = codecs.open("templates/Output.html", "a", "utf-8")
for i in range(1,3):
    url = 'http://notequangbang.blogspot.com/2017/0'+str(i)
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    contents = soup.find(class_ = 'posts')
    selected = contents.find_all('a')
    for select in selected:
        print(select['href'])
        pageget = requests.get(select['href'])
        ssoup = bs4.BeautifulSoup(pageget.content, 'html.parser')
        contenttitle = ssoup.find(class_ ="post-title entry-title")
        contentsget = str(ssoup.find(class_ ='post-body-inner'))
        print(contenttitle)
        print(contentsget)
        myfile.write('%s %s'%(contenttitle,contentsget))
myfile.close()