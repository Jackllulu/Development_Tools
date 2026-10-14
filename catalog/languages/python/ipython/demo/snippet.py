"""在 IPython 中: %run snippet.py"""


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print("fib(10) =", fib(10))
