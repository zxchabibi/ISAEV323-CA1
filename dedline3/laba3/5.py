import time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
def tail_fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return tail_fibonacci(n - 1, b, a + b)
n = 35
start_time = time.time()
result1 = fibonacci(n)
print(f"Fibonacci({n}) = {result1}")
print(f"Time taken (Naive): {time.time() - start_time:.6f} seconds")
start_time = time.time()
result2 = tail_fibonacci(n)
print(f"Tail Fibonacci({n}) = {result2}")
print(f"Time taken (Tail): {time.time() - start_time:.6f} seconds")