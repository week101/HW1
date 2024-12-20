# Сумма простых чисел в диапазоне от 2 до N включительно
# Необходимо разработать скрипт primes_sum.py, который для заданного значения аргумента командной строки и вычислит сумму всех простых числе в интервале [2,N].
import math

def primes(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    summa = 0
    for i in range(2, n + 1):
        if primes(i):
            summa += i
    return summa

n = int(input())
sum = sum_of_primes(n)
print(sum)
