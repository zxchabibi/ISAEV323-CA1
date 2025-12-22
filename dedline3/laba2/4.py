def my_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step
for i in my_range(1, 3, 0.5):
    print(i)