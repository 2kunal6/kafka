# Adapted from https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

import csv
import sys

from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'\t{row[1]}, {row[0]}')
        data = {row[1] : row[0]}
        producer.send('checkMessageProcessing', value=data)
        producer.send('fincompareEmailIds', value=data)

    producer.flush()