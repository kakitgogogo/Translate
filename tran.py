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

init='\033[0m'
black='\033[30m'
red='\033[31m'
green='\033[32m'
yellow='\033[33m'
blue='\033[34m'
purple='\033[35m'

def color_print(str,color=black):
	print color+str+'\033[0m'

try:
	page=urllib2.urlopen(url)
except Exception:
	print "翻译失败"

data=json.loads(page.read())
'''
output=json.dumps(data,indent=4)
fd=open("data.json","w")
fd.write(output)
'''
if sys.argv[1].isalpha():
	try:
		ph_en=data["symbols"][0]["ph_en"]
		if ph_en:
			color_print('['+ph_en+']',green)
		ph_am=data["symbols"][0]["ph_am"]
		if ph_am:
			color_print('['+ph_am+']',green)
		parts=data["symbols"][0]["parts"]
		for item in parts:
			print (yellow+"%-5s"+init)%item["part"],
			string=str()
			for mean in item["means"]:
				string+=mean+'; '
			color_print(string,blue)
	except Exception:
		color_print("翻译失败",red)

else:
	try:
		means=data["symbols"][0]["parts"][0]["means"]
		i=1
		color_print("Results:",yellow)
		for item in means:
			color_print(str(i)+". "+item["word_mean"],blue)
			i+=1
		color_print("Pronunciation: ",yellow)
		pron='['+data["symbols"][0]["word_symbol"]+']'
		color_print(pron,blue)
	except Exception:
		color_print("翻译失败",red)
		
