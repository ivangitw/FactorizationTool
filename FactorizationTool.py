import sys
from math import sqrt

error = 'fact.error'  # виняткова ситуація

def fact(n):
    if n < 1:
        raise ValueError(error)  # fact(): аргумент має бути >= 1
    if n == 1:
        return []

    res = []

    # Обробити парні множники спеціальним чином так,
    # щоб ми могли використати i = i+2 пізніше
    while n % 2 == 0:
        res.append(2)
        n = n // 2

    # Пробуємо непарні числа аж до sqrt(n)
    limit = sqrt(float(n + 1))
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n = n // i
            limit = sqrt(n + 1)
        else:
            i = i + 2

    if n != 1:
        res.append(n)

    return res

def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            n = int(arg)
            print(n, fact(n))
    else:
        try:
            while True:
                n = int(input())
                print(n, fact(n))
        except EOFError:
            pass

if __name__ == "__main__":
    main()
