from math import sqrt


def get_fibo(n):
    return int(((1+sqrt(5))**n - (1-sqrt(5))**n) / (2**n*sqrt(5)))

#print(get_fibo(5))
