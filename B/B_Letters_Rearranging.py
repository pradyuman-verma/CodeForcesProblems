from collections import Counter
from random import sample
def ans(arr):
    arr = sorted(arr)
    t = arr[::-1]
    if(arr == t):
        return -1
    return(''.join(arr))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(ans(s))