def process(n):
    if n % 3 == 0:
        return "fizz"
    return n

for number in range(1, 10):
    print(process(number))