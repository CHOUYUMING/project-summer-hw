#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:49:07 2019

@author: gsk
"""

import requests

site="http://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data"
response = requests.post(site)
#print(response.text)

with open('123.txt', 'w') as f:
    f.writelines(response.text)
    
#input("code:")