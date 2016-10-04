import cookielib
import urllib2 
import urllib 
import re
from bs4 import BeautifulSoup


from crawler_lib import *

class crawler_title(crawler_page):

	def __init__(self,outdir,urlStart):
         crawler_page.__init__(self,outdir);
         self.urlStart = urlStart
         self.MaxPageNum=0;
         self.urlBase = [];
         self.realRecord = 0;
         self.recordNum = 0;
         
	def urlGenerate(self):
         page = self._crawler_page__getpage_(self.urlStart+"1.html")
         page =page.decode('gb2312','ignore')
         soup  = BeautifulSoup(page)
         k=soup.find_all('div',class_="subFen")[0].text
         (m,n)=re.findall(u"\u5171 (\d*?) \u9875, (\d*?) \u6761",k)[0]
         page = int(m)
         record = int(n)
         self.MaxPageNum = page
         self.recordNum = record
         t = []
         for i in range(1,self.MaxPageNum+1):
             t.append(self.urlStart+'%s.html'%i);
         self.urlBase=t;
        
	def getData(self,text):
          soup = BeautifulSoup(text,"html.parser")
          dataDiv = soup.find_all("div",class_='club_dic');
          data = []
          for g in dataDiv:
              aData=g.findAll('h4')[0].findAll("a")
              if len(aData)!=2:
                  pass
              kemu = aData[0].text
              link = aData[1].attrs["href"]
              title= aData[1].text
              data.append([kemu,link,title])              
                    
          
          return data;
         

	def dealWithItem(self,item):
          d= item[2];
          d = d.replace("\t","")
          item[2] = d.replace("\n","")
          return '\t'.join(item).encode("utf-8")+'\n';



if __name__ == '__main__':
    
	pass
     #t=crawler_title()
     #t.run();

'''
==
'''



