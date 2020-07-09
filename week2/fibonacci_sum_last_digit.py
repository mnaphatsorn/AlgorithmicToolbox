# Uses python3
import sys
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


def fibonacci_sum(n):
    pisano =  pisanoperiod(10)
    length = len(pisano)
    sum_pisano = 0
    for i in range(length):
        sum_pisano +=  pisano[i]
    q = n//length
    sum = q*sum_pisano
    r = n % length
    for i in range(r+1):
        sum+=pisano[i]
    return sum%10

    

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
