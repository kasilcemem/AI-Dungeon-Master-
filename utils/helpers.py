import random
import time

def rand(lst):
    return random.choice(lst)

def randint(a, b):
    return random.randint(a, b)

def delay(ms):
    time.sleep(ms / 1000)
