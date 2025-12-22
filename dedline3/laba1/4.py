import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения функции {func.__name__}: {end - start:.4f} сек")
        return result
    return wrapper
@timer
def slow_func():
    for _ in range(1000000):
        pass
slow_func()