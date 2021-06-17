
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

def results(n):
    for i in range(0, n // 3 + 1):
        for j in range(0, n // 5 + 1):
            for k in range(0, n // 7 + 1):
                if((3 * i) + (5 * j) + (7 * k) == n):
                    return([i, j, k])
    return([-1])
    # tmp = {7 : [0, 0 , 1], 5: [0, 1, 0], 3: [1, 0, 0], 8:[1, 1, 0], 12:[0, 1, 1]}
    # for i in tmp.keys():
    #     if(n - i <= 0):
    #         continue
    #     if((n - i) % 3 == 0):
    #         tmp[i][0] += (n - i) // 3
    #         return(tmp[i])
    #     elif((n - i) % 5 == 0):
    #         tmp[i][1] += (n - i) // 5
    #         return(tmp[i])
    #     elif((n - i) % 7 == 0):
    #         tmp[i][2] += (n - i) // 7
    #         return(tmp[i])
    # return([-1])

def main():
    t = inp()
    for _ in range(t):
        n = inp()
        result = results(n)
        print(*result)

if __name__ == '__main__':
    main()