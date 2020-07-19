This program consumes reads from a csv file and puts unique EmailIds to a relational DB. Kafka is used as a buffer to hold messages.

Steps to run:
- start mysql: sudo systemctl start mysql
- check if zookeeper is up and if not then start it.
- start kafka: sudo systemctl start kafka
- run producer: python producer.py your-csv-filepath
- run consumer: python consumer.py
- run checker: python check_message_processing.py 
