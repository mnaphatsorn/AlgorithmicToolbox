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


def fibonacci_partial_sum(initial, final):
    pisano = pisanoperiod(10)
    length = len(pisano)
    q = (final//length)*length
    # print(q)
    sum_pisano = 0
    for k in range(length):
        sum_pisano+=pisano[k]
    sum = 0
    i = initial
    while i <= final:
        if i % length == 0 :
            x = q-i+1
            x = int(x/length)+1
            # print(x)
            sum += int(x)* sum_pisano
            i = q+1
            continue
        else:
            sum += pisano[i%length]
            i +=1
            # print(i%length)
    return sum % 10


if __name__ == '__main__':
    input = input()
    initial, final = map(int, input.split())
    print(fibonacci_partial_sum(initial, final))