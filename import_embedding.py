import sqlalchemy
from google.cloud.alloydb.connector import Connector

def getconn():
   connector = Connector()
   conn = connector.connect(
      "projects/<<PROJECTID>>/locations/us-east4/clusters/embedding-test/instances/embedding-instance",
      "pg8000",
      user="USER",
      password="PASSWORD",
      db="postgres",
      ip_type="PUBLIC"
   )
   return conn

def inserttodb(thought: str):
   # insert statement
   pool = sqlalchemy.create_engine(
      "postgresql+pg8000://",
      creator=getconn,
   )
   insert_stmt = sqlalchemy.text(
      "INSERT INTO thought_embedding (thought, entry_date) VALUES (:thought, now());",
      )
   with pool.connect() as db_conn:
      try:
         print(thought)
         trans = db_conn.begin()
         result = db_conn.execute(insert_stmt, parameters={"thought": thought})
         trans.commit()
         return True
      except Exception as e:
         print(e)
         return False
      
def getembedding():
   pool = sqlalchemy.create_engine(
      "postgresql+pg8000://",
      creator=getconn,
   )
   with pool.connect() as db_conn:
      sql= "SELECT thought, embedding FROM thought_embedding"
      embedding_data = db_conn.execute(sqlalchemy.text(sql)).fetchall()
      return embedding_data
   
def similar_thoughts(thought):
   pool = sqlalchemy.create_engine(
      "postgresql+pg8000://",
      creator=getconn,
   )
   with pool.connect() as db_conn:
      sql= "SELECT thought, entry_date FROM thought_embedding WHERE entry_date::DATE < NOW()::DATE ORDER BY embedding <-> (SELECT embedding FROM thought_embedding WHERE thought = '"+thought+"') LIMIT 3;"
      similar_thought = db_conn.execute(sqlalchemy.text(sql)).fetchall()
      return similar_thought
   return "No similar thoughts found"