#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import sys
import urllib2
import getopt

if len(sys.argv)>=2:
	word=sys.argv[1]
elif len(sys.argv)==1:
	word=raw_input("输入查询词：")

key="0EAE08A016D6688F64AB3EBB2337BFB0";
url="http://dict-co.iciba.com/api/dictionary.php?w="+word+"&key="+key+"&type=json"

try:
	page=urllib2.urlopen(url)
except Exception:
	print "翻译失败"

data=json.loads(page.read())

def yellow_print(str):
	print '\033[33m'+str+'\033[0m'

def blue_print(str):
	print '\033[34m'+str+'\033[0m'

yellow_print("Means:")
means=data["symbols"][0]["parts"][0]["means"]
i=1
for item in means:
	blue_print(str(i)+". "+item["word_mean"])
	i+=1;

yellow_print("Pronunciation: ")
pron=data["symbols"][0]["word_symbol"]
blue_print(pron)