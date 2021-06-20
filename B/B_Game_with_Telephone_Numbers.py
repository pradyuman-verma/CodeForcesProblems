
#import sys
# import math
# import bisect
# import collections
# import itertools
# #from sys import stdin,stdout
# from math import gcd,floor,sqrt,log
# from collections import defaultdict as dd, Counter as ctr
# from bisect import bisect_left as bl, bisect_right as br
# from itertools import permutations as pr, combinations as cb

#sys.setrecursionlimit(100000000)

#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$

inp    = lambda: int(input())
# strng  = lambda: input().strip()
# jn     = lambda  x,l: x.join(map(str,l))
strl   = lambda: list(input().strip())
# mul    = lambda: map(int,input().strip().split())
# mulf   = lambda: map(float,input().strip().split())
seq    = lambda: list(map(int,input().strip().split()))
#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
# p_inf = float('inf')
# n_inf = float('-inf')
#To find mex 
# def mex(arr):
#     nList = set(arr)
#     mex = 0
#     while mex in nList:
#         mex += 1
#     return(mex)

def results(arr, n):
    if(n < 11):
        return('NO')
    if(n == 11):
        if(arr[0] == 8):
            return('YES')
        return('NO')
    cnt = 0
    mov = n - 11
    my = (n - 11) // 2
    cnt2 = 0
    for i in range(n):
        if(arr[i] == '8'):
            cnt += 1
            if(i > mov):
                cnt2 += 1
    if(cnt < my):
        return('NO')
    else:
        if(cnt - cnt2 > my):
            return('YES')
        return('NO')

def main():
    n = inp()
    a = input()
    result = results(a, n)
    print(result)

if __name__ == '__main__':
    main()