"""
Cuarta Pregunta – Números de Fibonacci Pan-digitales

https://stackoverflow.com/questions/4935957/fibonacci-numbers-with-an-one-liner-in-python-3
https://codereview.stackexchange.com/questions/31614/improve-pandigital-algorithm

"""
from functools import reduce

fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]

def is_pandigital(nr, n):
    nr = str(nr)
    beg=set(nr[0:n])
    end=set(nr[-n:])
    return beg==end and beg==set(map(str, range(1, n + 1)))


for i in range(329460, 999999):
    s = str(fib(i))
    s_len = len(s)

    if len(s) >= 18:
        # if is_pandigital(s[0:9], 9):
        #     print("Inicio", i)
        # if is_pandigital(s[s_len-9:s_len], 9):
        #     print("Ultimo", i)
        if is_pandigital(s[0:9], 9) and is_pandigital(s[s_len-9:s_len], 9):
            print("Numero Fibonacci con pandigital al inicio y final: {}".format(i))

