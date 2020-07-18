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

for message in consumer:
    message = message.value
    for key in message:
        insert_cmd = "INSERT INTO EmailStorage VALUES('" + key + "', '" +  message[key] + "')"
        print(insert_cmd)
        try:
            mycursor.execute(insert_cmd)
            mydb.commit()
        except mysql.connector.IntegrityError as e:
            print(key + " already exists.")
