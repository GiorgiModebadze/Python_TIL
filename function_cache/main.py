from functools import cache
import time
from typing import Callable


@cache
def fib_cached(n: int) -> int:
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def time_function_ns(func: Callable, n: int) -> None:
    start = time.perf_counter_ns()
    print(func(n))
    end = time.perf_counter_ns()
    print(f"Function {func.__name__}  took {end - start} ns")


if __name__ == "__main__":
    fib_to_find: int = 30
    time_function_ns(fib, fib_to_find)
    time_function_ns(fib_cached, fib_to_find)
