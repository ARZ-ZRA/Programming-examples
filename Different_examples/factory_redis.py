import random
from datetime import datetime
from random import choice
import redis
from time import sleep
factory = redis.Redis(db=1)
candies = ['AAA', 'SSS', 'QQQ', 'WWW', 'EEE']
while True:
    sec = random.random()
    sleep(sec)
    for can in random.choices(candies):
        can_b = can.encode('utf-8')
        factory.rpush('candies', can_b)
        print(f"Type of candies ,{can_b}, at, {datetime.now()}")
