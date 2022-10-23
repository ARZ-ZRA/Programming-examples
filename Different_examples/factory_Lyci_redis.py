from datetime import datetime
from time import sleep

import redis
lucy = redis.Redis(db=1)
while True:
    sleep(0.5)
    con_b = lucy.blpop('candies', 10)
    remaining = lucy.llen('candies')
    if con_b:
        g = con_b[1]
        print("Lucy got a ", g, 'at', datetime.utcnow(), ',only ', remaining, ' left')
    else:
        print('Fin')
