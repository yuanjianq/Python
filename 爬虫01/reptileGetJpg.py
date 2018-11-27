#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import urllib.request
import re

def get_html(url):
	#打开网页
	page = urllib.request.urlopen(url)
	#读取页面源码
	html = page.read()
	html = html.decode('utf-8')
	return html

def get_image(html_code):
	#正则表达式
	reg = r'src="(.+?\.jpg)" width'
	#编译一下，运行更快
	reg_img = re.compile(reg)
	#进行匹配
	imglist = reg_img.findall(html_code)
	x = 0
	for img in imglist:
		#在控制台输出
		print(img)
		urllib.request.urlretrieve(img, '%s.jpg' %x)
		x += 1

print(u'-------网页图片抓取-------')
print(u'请输入url:'),
url = input()
if url:
    pass
else:
    print(u'---没有地址输入正在使用默认地址---')
    url = 'http://tieba.baidu.com/p/1753935195'
print(u'----------正在获取网页---------')
html_code = get_html(url)
print(u'----------正在下载图片---------')
get_image(html_code)
print(u'-----------下载成功-----------')
input('Press Enter to exit')


