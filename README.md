# healthcareQA
爬取寻医问药网的问答的python代码
##爬虫说明
爬虫会根据制定的起始日期到寻医问药网上抓取问题的链接，存入到basepath＋datapath之下，按照每天一个文件夹的存储，文件名为title.txt.数据格式如下：
科室\t链接\t问题\n
然后系统会扫描basepath＋datapath之下所有的title文件，抽取出其中的链接，逐个爬取链接对之下的问题和医生回复。然后存储为json形式的数据。数据格式如下：
 |-- answer: array (nullable = true)  
 |    |-- element: struct (containsNull = true)  
 |    |    |-- answer_text: string (nullable = true)  
 |    |    |-- answer_time: string (nullable = true)  
 |    |    |-- mainpage: string (nullable = true)  
 |    |    |-- major: string (nullable = true)  
 |    |    |-- name: string (nullable = true)  
 |    |    |-- position: string (nullable = true)  
 |-- question: struct (nullable = true)  
 |    |-- question: string (nullable = true)  
 |    |-- time: string (nullable = true)  
 |-- userinfo: struct (nullable = true)  
 |    |-- age: string (nullable = true)  
 |    |-- gender: string (nullable = true)  
 |    |-- name: string (nullable = true)  
 
##代码说明
配置文件config.py
系统调度文件crawler.py，main入口
爬虫父类crawler_page，位于crawler_lib.py
爬取链接类crawler_title位于crawler_title.py，继承crawler_page
爬取内容问答类crawler_content位于crawler_content.py，继承crawler_page

##操作步骤
step 1 . 修改配置文件config.py
basepath = '/home/healthcare/healthcare/' ＃ 修改为项目的安装目录
datapath = 'data/'     ＃ 该目录为数据存储目录          
title_file = 'title.txt'
content_file = 'content.txt'

＃ 爬取的起始日期
startDate = [2016,4,1] 
endDate  = [2016,4,30]


logFile = "logFile.txt" ＃ 链接爬取记录文件

logFile2 = "logFile2.txt" ＃ 内容爬取记录文件

step2. 在项目的安装目录下，创建名为‘data’的文件夹。

step3. 爬取链接目录文件
python ./code/crawler.py title >crawler_title.log

step4. 爬取内容文件
python ./code/crawler.py content >crawler_content.log
