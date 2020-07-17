import csv
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

with open('../resources/data_example.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'\t{row[1]}, {row[0]}')
        data = {row[1] : row[0]}
        producer.send('fincompareEmailIds', value=data)
        producer.flush()
