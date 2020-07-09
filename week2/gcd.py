# Uses python3
import sys

def gcd(a, b):
    if a < b:
        c = a
        a = b
        b = c
    remainder = a % b
    if remainder == 0:
        return b
    a = b
    b = remainder
    return gcd(a,b)
    

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd(a,b))
