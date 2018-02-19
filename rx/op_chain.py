# !/usr/bin/env python
# coding=utf-8

from rx import Observable



source = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

lengths = source.map(lambda s: len(s))

filtered = lengths.filter(lambda i: i >= 5)

filtered.subscribe(lambda value: print("Received {0}".format(value)))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-1))

from rx import Observable
from random import randint


three_emissions = Observable.range(1, 3)

three_random_ints = three_emissions.map(lambda i: randint(1, 100000)).publish()

three_random_ints.subscribe(lambda i: print("Subscriber 1 Received: {0}".format(i)))
three_random_ints.subscribe(lambda i: print("Subscriber 2 Received: {0}".format(i)))

three_random_ints.connect()

# letters = Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
#
# intervals = Observable.interval(1000)
#
# Observable.zip(letters, intervals, lambda s, i: (s, i)) \
#     .subscribe(lambda t: print(t))
#
# input("Press any key to quit\n")

# from sqlalchemy import create_engine, text
# from rx import Observable
#
# engine = create_engine('sqlite:///rexon_metals.db')
# conn = engine.connect()
#
#
# def customer_for_id(customer_id):
#     stmt = text("SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = :id")
#     return Observable.from_(conn.execute(stmt, id=customer_id))
#
#
# # Query customers with IDs 1, 3, and 5
# Observable.from_([1, 3, 5]) \
#     .flat_map(lambda id: customer_for_id(id)) \
#     .subscribe(lambda r: print(r))

import multiprocessing
import random
import time
from threading import current_thread

from rx import Observable
from rx.concurrency import ThreadPoolScheduler


def intense_calculation(value):
    # sleep for a random short duration between 0.5 to 2.0 seconds to simulate a long-running calculation
    time.sleep(random.randint(5, 20) * .1)
    return value


# calculate number of CPU's, then create a ThreadPoolScheduler with that number of threads
optimal_thread_count = multiprocessing.cpu_count()
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

# Create Process 1
Observable.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]) \
    .map(lambda s: intense_calculation(s)) \
    .subscribe_on(pool_scheduler) \
    .subscribe(on_next=lambda s: print("PROCESS 1: {0} {1}".format(current_thread().name, s)),
               on_error=lambda e: print(e),
               on_completed=lambda: print("PROCESS 1 done!"))

# Create Process 2
Observable.range(1, 10) \
    .map(lambda s: intense_calculation(s)) \
    .subscribe_on(pool_scheduler) \
    .subscribe(on_next=lambda i: print("PROCESS 2: {0} {1}".format(current_thread().name, i)),
               on_error=lambda e: print(e), on_completed=lambda: print("PROCESS 2 done!"))

# Create Process 3, which is infinite
Observable.interval(1000) \
    .map(lambda i: i * 100) \
    .observe_on(pool_scheduler) \
    .map(lambda s: intense_calculation(s)) \
    .subscribe(on_next=lambda i: print("PROCESS 3: {0} {1}".format(current_thread().name, i)),
               on_error=lambda e: print(e))

input("Press any key to exit\n")