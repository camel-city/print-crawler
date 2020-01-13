# 数据库操作文件db_cfg.py
#dialect+driver://username:password@host:port/database
################# mysql ##################
DIALECT = 'mysql'
DRIVE = 'mysqldb'
USERNAME = 'root'
PASSWORD = '000000'
HOST = '192.168.226.11'
PORT = '3306'
DATABASE = 'printercount'
 
DB_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVE,USERNAME,PASSWORD,HOST,PORT,DATABASE) 
SQLALCHEMY_DATABASE_URI = DB_URI 

#QLALCHEMY_DATABASE_URI = 'mysql://root:000000@127.0.0.1/test'
SQLALCHEMY_TRACK_MODIFICATIONS = False

################ mssql ######################
# SQLALCHEMY_DATABASE_URI = "mssql+pymssql://user:password123@127.0.0.1/DbOne"

#IALECT = 'mssql'
#RIVE = 'pymssql'
#SERNAME = 'sa'
#ASSWORD = 'edrive.2018'
#OST = '192.168.108.19'
#ORT = '1433'
#ATABASE = 'ICCO'

#B_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVE,USERNAME,PASSWORD,HOST,PORT,DATABASE)
#QLALCHEMY_DATABASE_URI = DB_URI
################ mssql end ####################
