import mysql.connector
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'fincompareEmailIds',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("USE FinCompare")
mycursor.execute("SELECT * FROM EmailStorage")

for message in consumer:
    message = message.value
    print(message)

for x in mycursor:
  print(x)
