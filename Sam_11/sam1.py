def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

fib = fib(200)

for num in fib:
    print(num)