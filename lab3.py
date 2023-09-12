from math import log
import time

# K, L, M natural or 0


def prime_factors(x):
    factors = []
    for k in range(int(log(x, 3)) + 1):
        for l in range(int(log(x, 5)) + 1):
            for m in range(int(log(x, 7)) + 1):
                temp = 3**k * 5**l * 7**m
                if temp < x:
                    factors.append(temp)
    return factors


x = float(input('Введите число: '))

now = time.time()
numbers = prime_factors(x)

print('Числа, удовлетворяющие условию: ', numbers)
print('Время выполнения алгоритма: ', time.time() - now)