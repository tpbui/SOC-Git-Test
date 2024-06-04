def process(n):
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    return n

if __name__ == '__main__':
    for number in range(1, 10):
        print(process(number))