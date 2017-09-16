#!/usr/bin/env python
#-*- coding:utf-8 -*-
import json
import sys, os
import requests
import getopt
import platform

sysinfo = platform.system()

key="0EAE08A016D6688F64AB3EBB2337BFB0"

init='\033[0m'
black='\033[30m'
red='\033[31m'
green='\033[32m'
yellow='\033[33m'
blue='\033[34m'
purple='\033[35m'

def color_print(str,color=black):
	if sysinfo == 'Linux':
		print(color+str+'\033[0m')
	else:
		print(str)

def en2cn(data):
	try:
		ph_en=data["symbols"][0]["ph_en"]
		if ph_en:
			color_print('['+ph_en+']',green)
		ph_am=data["symbols"][0]["ph_am"]
		if ph_am:
			color_print('['+ph_am+']',green)
		parts=data["symbols"][0]["parts"]
		for item in parts:
			color_print(("%-5s")%item["part"], yellow)
			string=str()
			for mean in item["means"]:
				string+=mean+'; '
			color_print(string,blue)
	except Exception as e:
		color_print("翻译失败:"+str(e),red)
		_, _, exc_tb = sys.exc_info()
		print('lineno:', exc_tb.tb_lineno)

def cn2en(data):
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
	except Exception as e:
		color_print("翻译失败:"+str(e),red)
		_, _, exc_tb = sys.exc_info()
		print('lineno:', exc_tb.tb_lineno)

def main():
	if len(sys.argv)>=2:
		word=sys.argv[1]
	elif len(sys.argv)==1:
		word=input("输入查询词：")
	url="http://dict-co.iciba.com/api/dictionary.php?w="+word+"&key="+key+"&type=json"

	try:
		page=requests.get(url)

		data=page.json()

		if not('\u4e00' <= word[0] <= '\u9fa5'):
			en2cn(data)
		else:
			cn2en(data)
	except Exception as e:
		color_print("翻译失败:"+str(e),red)
		exc_type, exc_obj, exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type, fname, exc_tb.tb_lineno)
		
if __name__=="__main__":
	main()