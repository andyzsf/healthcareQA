import cookielib
import urllib2 
import urllib 
import re
import datetime
def getpage(url):
	urllib2.socket.setdefaulttimeout(20)
	req = urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
	req.add_header('Connection','keep-alive')
	req.add_header('Cookie', '_s_tentry=y.qq.com; TC-V5-G0=6fd5dedc9d0f894fec342d051b79679e; Apache=3408937354106.456.1439532278021; SINAGLOBAL=3408937354106.456.1439532278021; ULV=1439532278118:1:1:1:3408937354106.456.1439532278021:; YF-V5-G0=db1555e71421c88d2c4b7e2202f0ee9d; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; YF-Page-G0=8ec35b246bb5b68c13549804abd380dc; login_sid_t=14cf17314b1f3aa37cff45cdb16fdb08; PHPSESSID=2fb603424f9c0cd2aea50f22744e64fb; TC-Ugrow-G0=02e35d9240e6933947925d24232af628; TC-Page-G0=9151a132144e87253eb430a7bc179e6b; WBStore=4e40f953589b7b00|undefined; WBtopGlobal_register_version=a3f5184be4b5f58b; SUHB=0JvRdSz5ISW9Bi; un=563109707@qq.com; myuid=2169193617; SUB=_2AkMigP6FdcNhrAFQnvEUxWjkbYpXzw73uNb4N07bZ2JCMnoQgT5nqiRotBF_DN7GjEe6utoadRGLELINFwldRz2cimJZ5nQ.; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WhxBpOdpizshjpSRI19.HoP5JpV2h-ce0271KM7SXWpMC4odcXt; ULOGIN_IMG=14405111225869; UOR=y.qq.com,widget.weibo.com,www.pythontab.com')
	result =urllib2.urlopen(req)
	text =result.read()
	return text
text =getpage('http://club.xywy.com/question/20160401/104779392.htm')
text = text.decode('gb2312','ignore')
p = re.compile('(<div class="f12 graydeep Userinfo clearfix pl29">.*?</div>)',re.S)
print re.findall(p,text)

p1 = re.compile('id="qdetailc">(.*?)</div>',re.S)
print re.findall(p1,text)[0]
p2 = re.compile('(<div class="Doc_con clearfix pr mt5 ">.*?)<script type="text/javascript">',re.S)
print re.findall(p2,text)[0]

print datetime.datetime.now()
for i in range(10):
	re.findall(p,text)
print datetime.datetime.now()
print datetime.datetime.now()
for i in range(500):
	re.findall(p,text)
print datetime.datetime.now()



