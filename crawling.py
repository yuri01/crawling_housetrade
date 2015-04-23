# -*- coding: utf-8 -*-

# import os
# os.getcwd()
# os.chdir("D:\\(DAS)HouseDataScrapping\\Python\\workingSpace")



#import csv
#import numpy as np
import pandas as pd
from pandas import DataFrame
import urllib as url
import json
from datetime import datetime


danjiCode = "ALL"
gubunRadio2 = "1"
tradelist = ['TradeAptLocal', 'RentAptLocal','TradeRhLocal','RentRhLocal','TradeShLocal','RentShLocal']
#tradelist = ['TradeAptLocal','TradeRhLocal','TradeShLocal'] ## 중요!!!!!!!! 
#tradelist = ['RentAptLocal','RentRhLocal','RentShLocal']   ## 중요!!!!!!!! 

df_donglist = pd.read_csv("D:\\(DAS)HouseDataScrapping\\Python\\workingSpace\\dongListExistOnly.txt",sep='\t', encoding='cp949')
df_donglist = df_donglist[[0,1,2,3,4]] #폐지여부는 필요없음
df_donglist.columns = ['dongcode','city','gu','dong','exist']
#df_donglist = df_donglist.dropna()


#t = 'TradeRhLocal'
#k = int(df_donglist["dongcode"][2])
#i = 2013
#j = 4


df_danji = pd.DataFrame()
df_detail = pd.DataFrame()
df1= pd.DataFrame()
df2= pd.DataFrame()
lstError = []

print ('START: ' + str(datetime.now()))

for t in tradelist:
    for k in df_donglist["dongcode"]:
        k = int(k)
        if k%10000==0:
            print(str(datetime.now()))        
        for i in range(2014, 2015):
            for j in range(3,5):
                if t == 'TradeAptLocal':
                    urls = "http://rt.molit.go.kr/rtApt.do?cmd=getTradeAptLocal&dongCode=" + str(k) + "&danjiCode=" + danjiCode + "&srhYear=" + str(i) + "&srhPeriod=" + str(j) + "&gubunRadio2=" + str(gubunRadio2)   
                    trade = 'TradeApt'
                elif t == 'RentAptLocal':
                    urls ="http://rt.molit.go.kr/rtApt.do?cmd=getRentAptLocal&dongCode=" + str(k) + "&danjiCode=" + danjiCode + "&srhYear=" + str(i) + "&srhPeriod=" + str(j) + "&gubunRadio2=" + str(gubunRadio2)
                    trade = 'RentApt'
                elif t == 'TradeRhLocal':
                    urls = "http://rt.molit.go.kr/rtRh.do?cmd=getTradeRhLocal&dongCode=" + str(k) + "&danjiCode=" + danjiCode + "&srhYear=" + str(i) + "&srhPeriod=" + str(j) + "&gubunRadio2=" + str(gubunRadio2)
                    trade = 'TradeRh'
                elif t == 'RentRhLocal':
                    urls = "http://rt.molit.go.kr/rtRh.do?cmd=getRentRhLocal&dongCode=" + str(k) + "&danjiCode=" + danjiCode + "&srhYear=" + str(i) + "&srhPeriod=" + str(j) + "&gubunRadio2=" + str(gubunRadio2)
                    trade = 'RentRh'
                elif t == 'TradeShLocal':
                    urls = "http://rt.molit.go.kr/rtSh.do?cmd=getTradeShLocal&dongCode=" + str(k) + "&srhYear=" + str(i) + "&srhPeriod=" + str(j) + "&gubunRadio2=" + str(gubunRadio2)
                    trade = 'TradeSh'
                elif t == 'RentShLocal':
                    urls = "http://rt.molit.go.kr/rtSh.do?cmd=getRentShLocal&dongCode=" + str(k) + "&srhYear=" + str(i) + "&srhPeriod=" + str(j) + "&gubunRadio2=" + str(gubunRadio2)
                    trade = 'RentSh'
                    
                #print urls
                urlStr = str(urls)
                try:
                    urlRes = url.urlopen(urlStr).read().decode('utf8')
                    urlJson = json.loads(urlRes)
                
                    danjiList = urlJson['danjiList']
                    detailList = urlJson['detailList']
                    
                    danji_keys = ['BOBN', 'BUBN','BUILD_YEAR','APT_CODE','APT_NAME','AREA_CNT','LAWD_CD','LAWD_NM','DONGCODE']
                    df_danji = DataFrame(danjiList, columns = danji_keys)

                    df_danji['TRADE'] = trade
                    df_danji['YEAR'] = i
                    df_danji['QUARTER'] = j
                    df_danji['DONGCODE'] = k

                    detail_keys = ['APT_CODE', 'AREA','SUM_AMT','FLOOR','DEPOSIT','MONTHLY','BOBN','BUBN','BUILD_YEAR','L_AREA','LAWD_CD','BLDG','TRADE','YEAR','MONTH','DAYS','DONGCODE']
                    df_detail = DataFrame(detailList, columns = detail_keys)
                    df_detail['TRADE'] = trade
                    df_detail['YEAR'] = i
                    df_detail['QUARTER'] = j                    
                    df_detail['DONGCODE'] = k

                except:
                    pass                

                if len(df_danji) == 0:
                    continue                #위의 for loop로 돌아가라는 것

                df1 = pd.concat([df1, df_danji], ignore_index=True)
                df2 = pd.concat([df2, df_detail], ignore_index=True)
                df_danji = pd.DataFrame()
                df_detail = pd.DataFrame()

                if len(df2) >= 100000:
                    danji ='danji'+str(datetime.now().strftime("%Y%m%d-%H%M%S"))+'.txt'
                    detail ='detail'+str(datetime.now().strftime("%Y%m%d-%H%M%S"))+'.txt'
                    df1.to_csv(danji, encoding='utf-8')
                    df2.to_csv(detail, encoding='utf-8')
                    df1 = pd.DataFrame()
                    df2 = pd.DataFrame()

danji ='danji'+str(datetime.now().strftime("%Y%m%d-%H%M%S"))+'.txt'
detail ='detail'+str(datetime.now().strftime("%Y%m%d-%H%M%S"))+'.txt'
df1.to_csv(danji, encoding='utf-8')
df2.to_csv(detail, encoding='utf-8')
df1 = pd.DataFrame()
df2 = pd.DataFrame()
#    ErrorList = 'ErrorList'+str(datetime.now().strftime("%Y%m%d-%H%M%S"))+'.txt'
#    lstError.to_csv(ErrorList, encoding='utf-8')
    
    
print("END: " + str(datetime.now()))
                    



