# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import urllib as url
import json
from pandas import DataFrame

'''
작업절차
(1) donglist가 있는 txt파일을 읽어옴: load_donglist()
(2) 좌표를 찾을 url을 생성: append_url_donglist(df_donglist)
(3) 동별 좌표를 다음api를 이용하여 찾아 저장: append_coordinate_to_donglist(df_donglist)
'''



def load_donglist():
  '''
  banbunjiList.txt 파일을 열어서 dataframe으로 반환
  '''
  df_donglist = pd.read_csv('banbunjiList2.CSV',sep=',', encoding='cp949')
  df_donglist = df_donglist[[0,1,2,3,4,5,6]] 
  df_donglist.columns = ['dongcode','city','gu','dong','ban1','ban2','APIkey']
#  df_donglist = df_donglist.dropna()
  return df_donglist
  
#def fill_donglist(df_donglist): 
#  '''
#  ban2에 빈값 '0' 채우기
#  '''
#  df_donglist['ban2']=df_donglist.ban2.str.strip()
#  for i in range(1,len(df_donglist['dongcode'])):
#      if type(df_donglist.ban2[i])==int:
#          if df_donglist.ban2[i]==0:
#              df_donglist['ban2'][i]=0
#      elif type(df_donglist.ban2[i])==unicode:
#          if len(df_donglist.ban2[i])==0:
#              df_donglist['ban2'][i]=0
#             
#  return df_donglist

def append_url_to_donglist(df_donglist):
  '''
  donglist에 좌표를 찾을 수 있는 url을 삽입
  '''

  df_donglist['url'] = df_donglist.apply(lambda x: 'http://apis.daum.net/local/geo/addr2coord?apikey='+x['APIkey']+'&q='+x['city']+
  '+'+x['gu']+'+'+x['dong']+'+'+str(int(x['ban1']))+'+'+str(int(x['ban2']))+'&output=json',axis=1)



#df_donglist['url']=''
#
#df_donglist.ix[:30000]['url']
#
#for i in range(0,len(df_donglist['dongcode'])):
#    if i<30000:
#        df_donglist['url'][i] = df_donglist.apply(lambda x: 'http://apis.daum.net/local/geo/addr2coord?apikey=eefc1b379855837997e9b23c8efc55f38c33773e&q='+x['city']+'+'+x['gu']+'+'+x['dong']+'+'+str(int(x['ban1']))+'+'+str(int(x['ban2']))+'&output=json',axis=1)
#
#    elif i//30000==1:
#        df_donglist['url'][i] = df_donglist.apply(lambda x: 'http://apis.daum.net/local/geo/addr2coord?apikey=2c6a0ebb9b9bab89f95162fe93102f2288d4ca0e&q='+x['city']+'+'+x['gu']+'+'+x['dong']+'+'+str(int(x['ban1']))+'+'+str(int(x['ban2']))+'&output=json',axis=1)
#
#    elif i//30000==2:
#        df_donglist['url'][i] = df_donglist.apply(lambda x: 'http://apis.daum.net/local/geo/addr2coord?apikey=8ff122467652a61d86bdf56311151eb4578d3a1f&q='+x['city']+'+'+x['gu']+'+'+x['dong']+'+'+str(int(x['ban1']))+'+'+str(int(x['ban2']))+'&output=json',axis=1)
#
#    elif i//30000>2:
#        df_donglist['url'][i] = df_donglist.apply(lambda x: 'http://apis.daum.net/local/geo/addr2coord?apikey=eefc1b379855837997e9b23c8efc55f38c33773e&q='+x['city']+'+'+x['gu']+'+'+x['dong']+'+'+str(int(x['ban1']))+'+'+str(int(x['ban2']))+'&output=json',axis=1)

  
        


  
def extract_coordinate_from_donglist(row):
  '''
  donglist 데이터프레임에서 한행씩 읽어와 google api를 통해 좌표를 공급받음
  '''
  urlStr = str(row['url'].encode('utf8'))
  urlRes = url.urlopen(urlStr).read().decode('utf8')
  urlJson = json.loads(urlRes)
  
#  print urlStr
  try:
	lat,lng = urlJson['channel']['item'][0]['lat'],urlJson['channel']['item'][0]['lng']
  except Exception as e:
    print 'Error', row['url']
    return 'None'
  return str(lat)+','+str(lng)
  
  
  
def append_coordinate_to_donglist(df_donglist):
 #df_donglist[['coorLat','coorLng']] = df_donglist.apply(extract_coordinate_from_donglist,axis=1)
 df_donglist['coorxy'] = df_donglist.apply(extract_coordinate_from_donglist,axis=1)
 
 return df_donglist
 
  

#def split_columns(df_donglist):
#    df=pd.DataFrame(df_donglist.coorxy.str.split(',',1).tolist(), columns=['lat','lng'])
#    
#    return df
#    

    
