# -*- coding: utf-8 -*-
"""
Created on Thu May 19 23:30:30 2016

@author: miaofu
"""


import re
import numpy as np
import demjson
import datetime
from bs4 import BeautifulSoup

from crawler_lib import *


def filter(txt):
    txt = txt.replace("\n","")
    txt =txt .replace("\t","")
    return txt
class crawler_content(crawler_page):

	def __init__(self,indir,outdir):
         crawler_page.__init__(self,outdir);
         self.indir = indir;
         self.urlBase=[];
         

	def urlGenerate(self):
         t = []
         f = open(self.indir,"r")
         content = f.readlines()
         
         for i in range(len(content)):
             c = content[i].split('\t')
             url = c[1]
             t.append(url)
         self.urlBase=t;
        
 
	def getData(self,text):
          # the url is key 
          # pantient
          p = re.compile('(<div class="f12 graydeep Userinfo clearfix pl29">.*?</div>)',re.S)
          user_text = re.findall(p,text)[0]
          #userinfo = soup.find_all("div",class_='f12 graydeep Userinfo clearfix pl29')
          #userinfo=userinfo[0];
          user_soup = BeautifulSoup(user_text)
          name = user_soup.find_all('span',class_='gray-a')[0].text
          span = user_soup.find_all('span')
          span = [i.text for i in span]
          age  = span[4]
          for i in span:
              if i.find(u'男')!=-1:
                  gender= u'男'
              if i.find(u'女')!=-1:
                  gender= u'女'
              if i.find(u'岁')!=-1:
                  age= i
          time = user_soup.find_all('span',class_='User_newbg User_time')[0].text;
          
          # question text
          #question = soup.find_all("div",id="qdetailc")[0].text# can be optimize with soup usersoup
          p1 = re.compile('id="qdetailc">(.*?)</div>',re.S)
          question = re.findall(p1,text)[0]
          
          # doc answer & doc info    
          p2 = re.compile('(<div class="Doc_con clearfix pr mt5 ">.*?)<script type="text/javascript">',re.S)
          answerDoc = re.findall(p2,text)
          if len(answerDoc)!=0:
             answerDoc = answerDoc[0]
             subsoup = BeautifulSoup(answerDoc)
             doctor   = subsoup.find_all("div",class_="Doc_zytpmd graydeep fl ml15 f14")
             doctorinfo=[]
             for d in doctor:
               tmp = d.find_all("a",class_='f14 fb Doc_bla')[0]
               doc_name = tmp.text
               doc_page = tmp.attrs["href"]
               position = d.find_all("span",class_="fl ml10 btn-a mr5")[0].text
               major    = d.find_all("p",class_="fl graydeep")[0].text
               doctorinfo.append([doc_name,doc_page,major,position])      
               # answer 
               answerDOM = subsoup.find_all("div",class_='pt10 mb5 clearfix pr qsdetail')
               answer    = []
               for a in answerDOM:
                 answer_text = a.find_all("div",class_='pt15 f14 graydeep  pl20 pr20')[0].text
                 answer_time = a.find_all("span",class_='User_newbg User_time Doc_time')[0].text
                 answer.append([answer_text,answer_time])
          else:
              doctorinfo=[]

          # conbime them
          data ={}
          data["userinfo"] = {"name":filter(name),"age":filter(age),"gender":gender};
          data["question"] = {"time":time,"question":filter(question)};
          data["answer"]   = []
          #print len(doctorinfo),len(answer)
          for i in range(len(doctorinfo)):
              d = doctorinfo[i]
              a = answer[i]
              data["answer"].append({"name":d[0],"mainpage":d[1],"major":d[2],"position":d[3],"answer_time":a[1],"answer_text":filter(a[0])})
          return [data];
         

	def dealWithItem(self,item):
          return demjson.encode(item).encode("utf-8")+"\n"
          



if __name__ == '__main__':
     url ='../tmp_data/'	
     t1= datetime.datetime.now()
     print t1
     t=crawler_content(url+"title.txt",url+"content.txt")
     t.run();
     print (datetime.datetime.now()-t1).total_seconds()


'''
	content = pd.DataFrame(content);
	content.to_excel("zhengce.xlsx",encoding="utf-8");

'''



