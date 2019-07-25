#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:21:58 2019

@author: gsk
"""
import requests
import json
import csv

year=input("年(ex:2019）:")
month=input("月(ex:07):")
day=input("日(ex:01,查詢整月份不必填寫）:")
stock_id=input("股票代碼:")
date=str(int(year)-1911)+"/"+month+"/"+day

url="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="+year+month+"01&stockNo="+stock_id
#url="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20190723&stockNo=2330"

res=requests.get(url)
s=json.loads(res.text)


    
with open('/Users/gsk/Desktop/output.csv', 'w') as f:
    outputwriter = csv.writer(f)
    outputwriter.writerow(s['title'])
    print(s['title'])
    outputwriter.writerow(s['fields'])
    print(s['fields'])
    if(day==""):
        for data in (s['data']):
            print(data)
            outputwriter.writerow(data)
            
    else:
        for data in (s['data']):
            if(data[0]==date):
                print(data)
                outputwriter.writerow(data)

        
#
    