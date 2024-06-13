from fastapi import FastAPI
import pandas as pd 
import sqlalchemy as sa

app = FastAPI()

@app.get("/")
async def root():

	conn_str = 'mysql+pymysql://user:user@hospital-db:3306/hospital'
	engine = sa.create_engine(conn_str)
	conn = engine.connect()
	hospital = pd.read_sql("chospital", conn)
	conn.close()

	return hospital.to_dict("records")
