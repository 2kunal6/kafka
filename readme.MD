This project reads from a csv file and puts unique EmailIds to a relational DB. Kafka is used as a buffer to hold messages.

Steps to run:
- start mysql: sudo systemctl start mysql
- check if zookeeper is up and if not then start it.
- start kafka: sudo systemctl start kafka
- run producer: python producer.py your-csv-filepath
- run consumer: python consumer.py
- run checker: python check_message_processing.py 

Explanation: 
- The Crux of this task is to put data inside a transaction and to handle DB failures.
- The producer.py program reads the csv and puts the messages in Kafka. The consumer.py program reads these messages and puts inside a DB. 
- Now, it may happen that consumer.py fails after consuming message from Kafka but before putting it in the DB. In that case, the message will be lost. To mitigate this, producer.py also puts the messages in a redundant topic called checkMessageProcessing, and a third program named check_message_programming.py checks if the messages are really inserted to DB and if not, then it puts back these messages to the original topic.
- The table has EmailId as a unique key (could be primary key too).

Things we could have done to make it better:
- In this code I have used MySQL, but to make it DB independent we could have used something like SQLAlchemy.
- Replicate the DB using mirroring to avoid data loss.
- We can optimize for performance by inserting in batches inside a Transaction.
- If write performance degrades we can use sharding and to make it read-efficient we could have made more read replicas.
- All the 3 programs could have been put in different Docker containers.
- Instead of reading from CSV it could have continuously listened from a MessageQueue.
- Kafka can be used in a cluster for more availability.
- Used Software Engineering principles like using properties file ConfigParser, putting hashed passwords in secrets, pytest, check incoming messages or csv files for any malicious values, use DB connector class, use Kafka connector class, flake, commit hooks etc.
- Configure Kafka to guarantee at least one read.
