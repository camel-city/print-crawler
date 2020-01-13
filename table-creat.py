import db_cfg
from sqlalchemy import create_engine
import sys
from flask_sqlalchemy import SQLAlchemy
#app.config.from_object(db_cfg)
#db = SQLAlchemy(app)
import requests        #导入requests包
from bs4 import BeautifulSoup


# creat_table_SQL = '''CREATE TABLE printcount (
#     id int AUTO_INCREMENT PRIMARY KEY,
#     print_ip varchar(100)  ,
#     print_name varchar(255) ,
#     black int(100),
#     colour int(100),
#     total_count int(100)
# );'''

creat_table_SQL = '''CREATE TABLE printer (
    id int AUTO_INCREMENT PRIMARY KEY,
    print_ip varchar(100)  ,
    print_name varchar(255) ,
    print_site varchar(255)
);'''

#creat_table_SQL = '''ALTER TABLE printcount CHANGE total_count total int(100)'''

engine = create_engine(db_cfg.DB_URI)

cus = engine.connect()
cus.execute(creat_table_SQL)
cus.close()

#ALTER TABLE <表名> ADD <新字段名> <数据类型> [约束条件] [FIRST|AFTER 已存在的字段名]；
# { ADD COLUMN <列名> <类型>
# | CHANGE COLUMN <旧列名> <新列名> <新列类型>
# | ALTER COLUMN <列名> { SET DEFAULT <默认值> | DROP DEFAULT }
# | MODIFY COLUMN <列名> <类型>
# | DROP COLUMN <列名>
# | RENAME TO <新表名> }

#db.session.execute(creat_table_SQL)


#创建与数据库的会话session class ,注意,这里返回给session的是个class类,不是实例
# Session_class = sessionmaker(bind=engine)       #创建用于数据库session的类
# session = Session_class()                       #这里才是生成session实例可以理解为cursor