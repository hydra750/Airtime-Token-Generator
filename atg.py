import random

n = 16
range_start = 10**(n-1)
range_stop = (10**n)-1

for _ in range(100):
    print(random.randrange(range_start, range_stop))