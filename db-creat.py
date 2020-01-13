from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database ,drop_database

DIALECT = 'mysql'
DRIVE = 'mysqldb'
USERNAME = 'root'
PASSWORD = '000000'
HOST = '192.168.226.11'
PORT = '3306'
DATABASE = 'printercount'



DB_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVE,USERNAME,PASSWORD,HOST,PORT,DATABASE)


#print (DB_URI)

#SQLALCHEMY_DATABASE_URI = DB_URI
engine = create_engine(DB_URI)
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))
