import urllib.request
import re
import dbm
#定义URL，其中%d用于替换页码
url = 'http://acm.zju.edu.cn/onlinejudge/showProblems.do?contestId=1&pageNumber=%d'
#html = urllib.request.urlopen(url).read()

#html = html.decode('utf-8')
#title = re.compile('<font color="blue">.*</font>')

#for x in title.findall(html):
#    title_parse = re.compile('<[^>]+>')
#    print(title_parse.sub('', x))
#连接持久化字典，这里用创建的方法'c'来创建写入
db = dbm.open('zoj_list', 'c')

for index in range(1, 30):
    this_url = url % (index)#替换URL中代表页码的数字
    html = urllib.request.urlopen(this_url).read()#read方法读取页面HTML
    html = html.decode('utf-8')#UTF-8编码，没有这句会提示错误
    title = re.compile('<font color="blue">.*</font>')#正则之，编译之
    key = ''
    cnt = 1
    for x in title.findall(html):
        title_parse = re.compile('<[^>]+>')#除去标签的正则
        get = title_parse.sub('', x)#除去标签
        if cnt % 2 == 0:
            value = get
            db[key] = value
        else:
            key = get
        cnt += 1
