from crawler_title import *
from crawler_content import *

import config

def dayGenerate(start,end):
    import datetime
    startDate = datetime.date(start[0],start[1],start[2]);
    endDate = datetime.date(end[0],end[1],end[2]);
    data = [];
    day =startDate
    while day<=endDate:
        data.append(day.strftime("%Y-%m-%d"))
        day = day + datetime.timedelta(days=1);
    return data
def clean(date):
    import os
    if os.path.exists(config.basepath+config.datapath+"/"+date+"/"):
        pass
    else:
        os.mkdir(config.basepath+config.datapath+"/"+date+"/")
    
def continueNum():
    import os
    if os.path.exists(config.basepath+config.logFile):
        f= open(config.basepath+config.logFile,"r");
        text = f.readlines();
        return len(text)
    else:
        return 0
    
def phase1():
    
   # main
   jobDays = dayGenerate(config.startDate,config.endDate)
   startNum = continueNum()

   for job_id in range(startNum,len(jobDays)):
    
     job = jobDays[job_id]
     print job
     clean(job);
     path  = config.basepath+config.datapath+job+"/"
    
     t=crawler_title(path+config.title_file,config.urlStart+job+"/")
     t.run()
     #   c = crawler_content(path+config.title_file,path+config.content_file)
     #  c.run()
     if t.getIsOver():
        f=open(t.outdir,'r')
        t.realRecord= len(f.readlines())
        f.close()
        f= open(config.basepath+config.logFile,"a");
        f.write(str(job_id)+"\t"+job+"\t"+str(t.MaxPageNum)+"\t"+str(t.recordNum)+"\t"+str(t.realRecord)+"\n")
        f.close()
def phase2():
    import os
    
    jobList = os.listdir(config.basepath+config.datapath);
    jobList.sort()
    jobList.reverse()# change this to 
    print jobList
    #return 0
    for job in jobList:
        job_id = jobList.index(job)
        print job_id,job
        path = config.basepath+config.datapath+job+"/"
        try:
          f  =open(path+config.title_file,'r')
        except:
          continue
        f.close()
        t = crawler_content(path+config.title_file,path+config.content_file)
        t.run()
        if t.getIsOver():
           f=open(t.outdir,'r')
           t.realRecord= len(f.readlines())
           f.close()
           f= open(config.basepath+config.logFile2,"a");
           f.write(str(job_id)+"\t"+job+"\t"+str(len(t.urlBase))+"\t"+str(t.realRecord)+"\n")
           f.close()
         
       
if __name__=="__main__":
   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument("p",choices=['title','content'],help='select title or content')
   args = parser.parse_args()
   if args.p =='title':
      phase1();
   if args.p =='content':
      phase2();

   
    
    
    
