from time import sleep
import datetime
import sqlalchemy as sa
import pandas as pd
from urllib.parse import quote

# ---------------------GET DATA----------------------------------

DIALECT = "mysql"
SQL_DRIVER = "pymysql"
USERNAME = "testuser"
PASSWORD = "P@ssw0rd"
HOST = "202.44.12.115"
PORT = 3306
DBNAME = "de_inter"

conn_str = DIALECT + "+" + SQL_DRIVER + "://" + USERNAME + ":" +quote(PASSWORD) + "@" + HOST + ":" +str(PORT) + "/" + DBNAME

# conn_str = 'mysql+pymysql://testuser:P@ssword@202.44.11.115:3306/de_inter'
engine = sa.create_engine(conn_str)
conn = engine.connect()
hospital = pd.read_sql("chospital", conn)
conn.close()

# ---------------------INSERT TO MY SQL----------------------------------
conn_str2 = "mysql+pymysql://user:user@hospital-db:3306/hospital"
engine2 = sa.create_engine(conn_str2)
conn2 = engine2.connect()
hospital.to_sql("chospital", conn2, index=False, if_exists="replace")
conn.close()