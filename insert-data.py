import db_cfg
from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine(db_cfg.DB_URI)
connection = engine.connect()
#"字段名":变量
data = [{"print_ip": '192.168.5.235',  "print_name": '行政',            "print_site": '行政' },
        {"print_ip": '172.19.112.95',  "print_name": 'SMT',             "print_site": 'SMT' },
        {"print_ip": '192.168.13.241', "print_name": '一楼市场',        "print_site": '一楼市场' },
        {"print_ip": '192.168.20.200', "print_name": '设备科',          "print_site": '设备科' },
        {"print_ip": '172.19.5.222',   "print_name": '2楼财务打印',     "print_site": '2楼财务打印' },
        {"print_ip": '192.168.60.11',  "print_name": '3号楼打印机',     "print_site": '3号楼打印机' },
        {"print_ip": '192.168.3.236',  "print_name": '3楼技术打印机',   "print_site": '3楼技术打印机' },
        ]
sql = text("""insert into printer (print_ip , print_name , print_site) VALUE (:print_ip , :print_name , :print_site)""")

for line in data:
        connection.execute(sql, **line)