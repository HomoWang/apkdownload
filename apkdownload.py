#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

url="http://apkpure.com/search?q="
browser=webdriver.Chrome()
count = 0
total = 0
error = 0
file = open('apklist.txt','r')  # 如果沒有第二個參數，表示預設的模式是 'r'
for line in file:
     total = total + 1
     #print line
     list1=line.split(',')
     if list1[0].find('\n'):
          apkfile=list1[0].split(".apk")[0]
     else:
          apkfile=list1[0]
     print apkfile
     print "total = " + str(total)
     browser.get(url+apkfile)
     sleep(1)
     cls2=browser.find_element_by_class_name("search-text")
     main_window = browser.current_window_handle
     tag=cls2.find_element_by_tag_name("span")
     print tag.text
     if tag.text=="1":
         count = count + 1
         print "count = " + str(count)
         print "find apk"
         browser.find_element_by_link_text("Read More").click()
         sleep(3)
         browser.switch_to_window(browser.window_handles[1])
         print browser.current_url
         browser.find_element_by_class_name(" da").click()
         sleep(5)
         browser.close()
         browser.switch_to_window(main_window)
     else:
          print "count = " + str(count)
          print "not find apk"
     print "-----------------------------------------------------------------------"     
file.close()
