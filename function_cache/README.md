# Function Cache 

```python

from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

```

for large numbers fib function will take excessive amount of time to calculate, using cache will cache each run and speed up process 

P.s This cuould have been done faster with generators as well