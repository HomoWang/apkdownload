#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests as rq
from time import sleep

link_ls = []
total = 0
url="https://play.google.com/store/apps/category/WEATHER"
response = rq.get(url)
print response
html_doc = response.text
soup = BeautifulSoup(response.text, "html.parser")

_cls_all = soup.findAll("a", {"class": "card-click-target"}) 

for _cls_each in _cls_all:
  total += 1
  link_ls.append("https://play.google.com" + _cls_each['href'].encode("ascii") + "\n")
  print "https://play.google.com" + _cls_each['href']

#print link_ls
print "---------------------------------------------------------"
print "sort total：" + str(sorted(set(link_ls),key=link_ls.index))
print "list len =" + str(len(link_ls))
print "Total =" + str(total)

for index in sorted(set(link_ls),key=link_ls.index):
  print index
  f = open(url.split('?')[0].split('/')[len(url.split('?')[0].split('/')[1])-1] + "list.txt","a+")
  f.write(index)
  f.close()
