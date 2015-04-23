# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 13:14:41 2014

@author: 0720046__
"""

# import os
# os.chdir('D:\\(DAS)HouseDataScrapping\\Python\\workingSpace')
# print os.getcwd()

import pandas as pd
from pandas import DataFrame

from os import listdir
from os.path import isfile, join

danjiResults=pd.DataFrame()
detailResults=pd.DataFrame()
finalResults=pd.DataFrame()


## [danji파일 합치기]
myfile="D:\\(DAS)HouseDataScrapping\\Python\\workingSpace\\danji"
onlyfiles=[f for f in listdir(myfile) if isfile(join(myfile,f))] # 파일제목리스트

for k in onlyfiles:  
    data=pd.read_csv(myfile+str("\\")+k, sep=',', encoding='utf-8')
    danjiResults=danjiResults.append(data, ignore_index=True)
print 'initial danjiResults=', danjiResults.shape


danjiResults=danjiResults.drop(['Unnamed: 0'], axis=1)
danjiResults['uniqueKey']=danjiResults.apply(lambda x: str(x['BOBN'])+'-'+str(x['BUBN'])+'&'+str(x['BUILD_YEAR'])+'&'+str(x['APT_CODE'])+'&'+str(x['DONGCODE']),axis=1) # 키 칼럼 생성
danjiResults=danjiResults.rename(columns={'BOBN': 'Danji_BOBN', 'BUBN':'Danji_BUBN','BUILD_YEAR':'Danji_BUILD_YEAR','APT_CODE': 'Danji_APT_CODE', 'APT_NAME':'Danji_APT_NAME','AREA_CNT':'Danji_AREA_CNT','LAWD_CD': 'Danji_LAWD_CD', 'LAWD_NM':'Danji_LAWD_NM','AREA_CNT':'Danji_AREA_CNT','DONGCODE':'Danji_DONGCODE','MONTH':'Danji_QUARTER','YEAR':'Danji_YEAR','QUARTER':'Danji_QUARTER'})
print str('final danjiResults='), danjiResults.shape

# [detail파일 합치기]
myfile2="D:\\(DAS)HouseDataScrapping\\Python\\workingSpace\\detail"    
onlyfiles2=[f for f in listdir(myfile2) if isfile(join(myfile2,f))]

for k in onlyfiles2:  # detail파일 하나로하기
    data=pd.read_csv(myfile2+str("\\")+k, sep=',', encoding='utf-8')
    detailResults=detailResults.append(data, ignore_index=True)

print str('initial datailResults='), detailResults.shape
detailResults=detailResults.drop(['Unnamed: 0'], axis=1)

## TRADE와 RENT 구분
danjiResults['type']=danjiResults['TRADE'].apply(lambda x:x[:4])
detailResults['type']=detailResults['TRADE'].apply(lambda x:x[:4])

danjiResults_T=danjiResults[danjiResults['type']=='Trad']
danjiResults_R=danjiResults[danjiResults['type']=='Rent']
detailResults_T=detailResults[detailResults['type']=='Trad']
detailResults_R=detailResults[detailResults['type']=='Rent']

danjiResults_T=danjiResults_T.drop('type', axis=1)
danjiResults_R=danjiResults_R.drop('type', axis=1)
detailResults_T=detailResults_T.drop('type', axis=1)
detailResults_R=detailResults_R.drop('type', axis=1)



#분기단위 파일저장

q=range(1,5)
for i in q:
    if i==1:
        DanjiT=danjiResults_T[danjiResults_T['Danji_QUARTER']==1]
        DetailT=detailResults_T[detailResults_T['QUARTER']==1]
        
        DanjiR=danjiResults_R[danjiResults_R['Danji_QUARTER']==1]
        DetailR=detailResults_R[detailResults_R['QUARTER']==1]        
        
        if len(DetailT)>0:
            y=DanjiT.iloc[0]['Danji_YEAR']
            print str('Q'), str(i), str('DanjiT='), DanjiT.shape, str('DetailT='), DetailT.shape
            print str('Q'), str(i), str('DanjiR='), DanjiR.shape, str('DetailR='), DetailR.shape            
            
            name1="Danji"+str(y)+"Q"+str(i)+"TRADE.txt"
            name2="Detail"+str(y)+"Q"+str(i)+"TRADE.txt"
            name3="Danji"+str(y)+"Q"+str(i)+"RENT.txt"
            name4="Detail"+str(y)+"Q"+str(i)+"RENT.txt"            
            
            DanjiT.to_csv(name1, encoding='utf-8')
            DetailT.to_csv(name2, encoding='utf-8')
            DanjiR.to_csv(name3, encoding='utf-8')
            DetailR.to_csv(name4, encoding='utf-8')
                        
            
    elif i==2:
        DanjiT=danjiResults_T[danjiResults_T['Danji_QUARTER']==2]
        DetailT=detailResults_T[detailResults_T['QUARTER']==2]
        
        DanjiR=danjiResults_R[danjiResults_R['Danji_QUARTER']==2]
        DetailR=detailResults_R[detailResults_R['QUARTER']==2]        
        
        if len(DetailT)>0:
            y=DanjiT.iloc[0]['Danji_YEAR']
            print str('Q'), str(i), str('DanjiT='), DanjiT.shape, str('DetailT='), DetailT.shape
            print str('Q'), str(i), str('DanjiR='), DanjiR.shape, str('DetailR='), DetailR.shape            
            
            name1="Danji"+str(y)+"Q"+str(i)+"TRADE.txt"
            name2="Detail"+str(y)+"Q"+str(i)+"TRADE.txt"
            name3="Danji"+str(y)+"Q"+str(i)+"RENT.txt"
            name4="Detail"+str(y)+"Q"+str(i)+"RENT.txt"            
            
            DanjiT.to_csv(name1, encoding='utf-8')
            DetailT.to_csv(name2, encoding='utf-8')
            DanjiR.to_csv(name3, encoding='utf-8')
            DetailR.to_csv(name4, encoding='utf-8')
            
    elif i==3:
        DanjiT=danjiResults_T[danjiResults_T['Danji_QUARTER']==3]
        DetailT=detailResults_T[detailResults_T['QUARTER']==3]
        
        DanjiR=danjiResults_R[danjiResults_R['Danji_QUARTER']==3]
        DetailR=detailResults_R[detailResults_R['QUARTER']==3]        
        
        if len(DetailT)>0:
            y=DanjiT.iloc[0]['Danji_YEAR']
            print str('Q'), str(i), str('DanjiT='), DanjiT.shape, str('DetailT='), DetailT.shape
            print str('Q'), str(i), str('DanjiR='), DanjiR.shape, str('DetailR='), DetailR.shape            
            
            name1="Danji"+str(y)+"Q"+str(i)+"TRADE.txt"
            name2="Detail"+str(y)+"Q"+str(i)+"TRADE.txt"
            name3="Danji"+str(y)+"Q"+str(i)+"RENT.txt"
            name4="Detail"+str(y)+"Q"+str(i)+"RENT.txt"            
            
            DanjiT.to_csv(name1, encoding='utf-8')
            DetailT.to_csv(name2, encoding='utf-8')
            DanjiR.to_csv(name3, encoding='utf-8')
            DetailR.to_csv(name4, encoding='utf-8')
            
    elif i==4:
        DanjiT=danjiResults_T[danjiResults_T['Danji_QUARTER']==4]
        DetailT=detailResults_T[detailResults_T['QUARTER']==4]
        
        DanjiR=danjiResults_R[danjiResults_R['Danji_QUARTER']==4]
        DetailR=detailResults_R[detailResults_R['QUARTER']==4]        
        
        if len(DetailT)>0:
            y=DanjiT.iloc[0]['Danji_YEAR']
            print str('Q'), str(i), str('DanjiT='), DanjiT.shape, str('DetailT='), DetailT.shape
            print str('Q'), str(i), str('DanjiR='), DanjiR.shape, str('DetailR='), DetailR.shape            
            
            name1="Danji"+str(y)+"Q"+str(i)+"TRADE.txt"
            name2="Detail"+str(y)+"Q"+str(i)+"TRADE.txt"
            name3="Danji"+str(y)+"Q"+str(i)+"RENT.txt"
            name4="Detail"+str(y)+"Q"+str(i)+"RENT.txt"            
            
            DanjiT.to_csv(name1, encoding='utf-8')
            DetailT.to_csv(name2, encoding='utf-8')
            DanjiR.to_csv(name3, encoding='utf-8')
            DetailR.to_csv(name4, encoding='utf-8')





