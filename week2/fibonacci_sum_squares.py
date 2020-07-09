# Uses python3
from sys import stdin
#(a*b)modc = ((a mod c)*(b mod c))mod c

def pisanoperiod(m):
    f = 1
    pisanoperiod = [0,1]
    for i in range(2,10**14):
        prev = f
        f = fibonacci(i) % m
        if (prev==0) and (f == 1):
            pisanoperiod.pop()
            return pisanoperiod
        pisanoperiod.append(f)
    return pisanoperiod

def fibonacci(n):
    if n<= 1:
        return n
    F=[0]*(n+1)
    F[1]=1
    for i in range (2,n+1):
        F[i] = F[i-1]+F[i-2]
    return F[n]

def get_remainder(n):
    pisano = list(pisanoperiod(10))
    remainder = pisano[n%len(pisano)] 
    return remainder

def fibonacci_sum_squares(n):
    width = get_remainder(n)
    length = get_remainder(n+1)
    sum_squares = width*length

    return  sum_squares%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
