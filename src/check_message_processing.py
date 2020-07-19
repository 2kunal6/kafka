# Adapted from https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

import mysql.connector

from json import loads
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'checkMessageProcessing',
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

for message in consumer:
    message = message.value
    for key in message:
        select_cmd = "SELECT * FROM EmailStorage VALUES('" + key + "', '" +  message[key] + "')"
        print(select_cmd)
        try:
            mycursor.execute(insert_cmd)
            mydb.commit()
        except mysql.connector.IntegrityError as e:
            print(key + " already exists.")
