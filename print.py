import db_cfg
from sqlalchemy import create_engine
from sqlalchemy import text
import datetime

import requests        #导入requests包
from bs4 import BeautifulSoup

engine = create_engine(db_cfg.DB_URI)
connection = engine.connect()

urla = 'http://'
urlb = '/sys_count.html'
urlc = '/main.html'

nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
checktime = nowTime
select_print = text("select print_ip , print_name from printer")
result = connection.execute(select_print)
resus = list(result)
# for resu in resus:
#     ipadd = (resu[0])
#     print_name = (resu[1])

    # url = str(urla) + str(ipadd) + str(urlb)
    # strhtml = requests.get(url)        #Get方式获取网页数据
    # strhtml.encoding = 'utf-8'
    # soup=BeautifulSoup(strhtml.text,'lxml')
url2 = 'http://192.168.5.235/main.html'
#url2 = 'http://192.168.5.235/sys_count.html'
#url2 = str(urla) + str(ipadd) + str(urlc)

strhtml2 = requests.get(url2, auth=('admin', 'admin'))        #Get方式获取网页数据
#strhtml2.encoding = 'utf-8'
soup2=BeautifulSoup(strhtml2.text,'lxml')

printids = soup2.select('body > form > div > div.main > table:nth-child(3) > tbody > tr:nth-child(1) > td:nth-child(2)')
#print (url2)
print (soup2)

print (printids)
    # for printid in printids:
    #     printidnumber = (printid.get_text())
    #     printi = (printidnumber)
    #
    #     print (soup2)

    # blacks = soup.select('body > form > div > div.main > table:nth-child(3) > tbody > tr:nth-child(1) > td:nth-child(2)')
    # for black in blacks:
    #     blacknumber = (black.get_text())
    #     black = (blacknumber)
    # colours = soup.select('body > form > div > div.main > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2)')
    # for colour in colours:
    #     colournumber = (colour.get_text())
    #     colour =  (colournumber)
    #
    # data = [{"print_ip": (resu[0]), "print_name": (resu[1]), "black": (black), "colour": (colour), "total": 0 , "check_time":(checktime)},
    #         ]
    # sql = text("""insert into printcount (print_ip , print_name , black , colour , total , check_time) VALUE (:print_ip , :print_name , :black , :colour , :total ,:check_time)""")
    #
    # for line in data:
    #     connection.execute(sql, **line)