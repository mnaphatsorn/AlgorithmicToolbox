# Uses python3
def fibonacci(n):
    if n<= 1:
        return n
    F=[0]*(n+1)
    F[1]=1
    for i in range (2,n+1):
        F[i] = F[i-1]+F[i-2]
    return F[n]

n = int(input())
print(fibonacci(n))
