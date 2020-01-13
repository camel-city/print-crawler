from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

DIALECT = 'mysql'
DRIVE = 'mysqldb'
USERNAME = 'root'
PASSWORD = '000000'
HOST = '192.168.226.11'
PORT = '3306'
DATABASE = 'ICCO'

engine = create_engine('mysql+mysqldb://user:passwd@localhost/mydatabase')

DB_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVE,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE printcount")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#  print(x)