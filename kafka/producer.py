import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))


for num in range(0, 10):
    if num % 2 == 0:
        future = producer.send('even', {"even": num})
    else:
        future = producer.send('odd', {"odd": num})

try:
    record_metadata = future.get(timeout=10)
except KafkaError as e:
    print(e)
    pass

print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)
