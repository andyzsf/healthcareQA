import cookielib
import urllib2 
import urllib 
import re
import numpy as np
from bs4 import BeautifulSoup

class crawler_page():

	def __init__(self,output):
		self.urlBase = [];
		self.outdir = output;
                self.totalNum = 0;
                f = open(self.outdir+"logUrl.txt","a");
                f.close()
                f = open(self.outdir,"a");
                f.close();
	def __getpage_(self,url):
	    urllib2.socket.setdefaulttimeout(20)
	    req = urllib2.Request(url)
	    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
	    req.add_header('Connection','keep-alive')
	    req.add_header('Cookie', '_s_tentry=y.qq.com; TC-V5-G0=6fd5dedc9d0f894fec342d051b79679e; Apache=3408937354106.456.1439532278021; SINAGLOBAL=3408937354106.456.1439532278021; ULV=1439532278118:1:1:1:3408937354106.456.1439532278021:; YF-V5-G0=db1555e71421c88d2c4b7e2202f0ee9d; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; YF-Page-G0=8ec35b246bb5b68c13549804abd380dc; login_sid_t=14cf17314b1f3aa37cff45cdb16fdb08; PHPSESSID=2fb603424f9c0cd2aea50f22744e64fb; TC-Ugrow-G0=02e35d9240e6933947925d24232af628; TC-Page-G0=9151a132144e87253eb430a7bc179e6b; WBStore=4e40f953589b7b00|undefined; WBtopGlobal_register_version=a3f5184be4b5f58b; SUHB=0JvRdSz5ISW9Bi; un=563109707@qq.com; myuid=2169193617; SUB=_2AkMigP6FdcNhrAFQnvEUxWjkbYpXzw73uNb4N07bZ2JCMnoQgT5nqiRotBF_DN7GjEe6utoadRGLELINFwldRz2cimJZ5nQ.; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WhxBpOdpizshjpSRI19.HoP5JpV2h-ce0271KM7SXWpMC4odcXt; ULOGIN_IMG=14405111225869; UOR=y.qq.com,widget.weibo.com,www.pythontab.com')
	    result =urllib2.urlopen(req)
	    text =result.read()
            return text

        def urlGenerate(self):
          raise NotImplementedError("urlGenerate should be overwritten!")


	def __getData_(self,text):
		y=[];
                text = text.decode('gb2312','ignore')
        
		#soup = BeautifulSoup(text);
		'''
		data = soup.find_all("div",class_='news_title');
		for i in data:
			s1=i.text;
			c = i.findNext()
			s2 = c.attrs["href"]
			y.append([s1,s2]);
		return y;
		'''
		return self.getData(text);

	# user define
	def getData(self,text):
		pass;


	def __toText_(self,data,path):
		f= open(path,'a');
		for i in data:
			#f.write(i[0].encode("utf-8")+'\t'+i[1]+'\n');
			string = self.dealWithItem(i);
			f.write(string);

		f.close();
		return 1
	# user define, A STRING SHOULD BE RETURNED
	def dealWithItem(item):
		raise NotImplementedError("urlGenerate should be overwritten!");



        def dealWrong(self):
            pass
        def __continue_(self):
            import os
            if not os.path.exists(self.outdir+"logUrl.txt"):
                self.lastNum =0 
                total =0
                success = 0
            else:
              f = open(self.outdir+"logUrl.txt","r")
              text = f.readlines()
              total = len(text)
              success = 0
              for i in text:
                 data = i.split('\t')
                 if data[0]=='success':
                    success+=1
              self.lastNum  = total
            print "init state report"
            print "total"+"\t"+"done"+"\t"+"success"+"\t"+"fail"
            print len(self.urlBase),'\t',total,'\t',success,'\t',total-success

	def run(self):
            flag = self.getIsOver()
            if flag:
               pass
            else:
		
                lenUrl = len(self.urlBase)
		for i in range(self.lastNum,lenUrl):
                        url = self.urlBase[i]
                        if i%200==0:
                            print 'Process:',i,"/",lenUrl 
                        log="success"+'\t'+str(i)+"\t"+str(lenUrl)+'\t'+url+"\n"
			try:
			   text  = self.__getpage_(url);
			   item  = self.__getData_(text);
                           self.__toText_(item,self.outdir);     
			except:
                           print "parse error"
                           log="fail"+'\t'+str(i)+"\t"+str(lenUrl)+'\t'+url+"\n"
                        f = open(self.outdir+"logUrl.txt","a");
                        f.write(log)
	         	f.close();
        def getIsOver(self):
            self.urlGenerate();
            self.__continue_();
            return self.lastNum==len(self.urlBase)        
        











