import dramatiq
import requests

from dramatiq.brokers.redis import RedisBroker


redis_broker = RedisBroker(host='127.0.0.1', port=6379)
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def count_num():
    url = 'https://ya.ru/'
    response = requests.get(url)
    len_text = len(response.text)
    print(f'Len text {len_text}')

count_num.send()