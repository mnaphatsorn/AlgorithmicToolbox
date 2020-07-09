# Uses python3
import sys

def pisanoperiod(n,m):
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

def get_fibonacci_huge(n, m):
    pisano = list(pisanoperiod(n,m))
    # print(pisano)
    # print(len(pisano))
    # print(n%m)
    remainder = pisano[n%len(pisano)] 
    return remainder

if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
    # l = []
    # for i in range(97,202):
    #     l.append(fibonacci(i)%100)
    # print(l)