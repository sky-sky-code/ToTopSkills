import argparse
from pathlib import Path
import dramatiq
from dramatiq.brokers.redis import RedisBroker

from dramatiq.cli import main, make_argument_parser

if __name__ == '__main__':
    redis_broker = RedisBroker(host='127.0.0.1', port=6379)
    dramatiq.set_broker(redis_broker)

    args = make_argument_parser().parse_args()
    main(args)