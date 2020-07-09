# Uses python3
import sys

def get_change(m):
    coins=0
    while m >0:
        if m >=10:
            coins+= m//10
            m = m%10
        elif m>=5:
            coins+=m//5
            m = m%5
        else:
            coins += m 
            m =0
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
