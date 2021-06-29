
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

def results(arr, n, m):
    cnt = 0 
    for i in range(1, n):
        for j in range(m):
            if(arr[i][j] == '*'):
                cnt += abs((sum([x for x in range(j)]) - 1) * (sum([x for x in range(m - j)]) - 1))
    return cnt

def main():
    nm = seq()
    n, m = nm[0], nm[1]
    a = []
    for i in range(n):
        a.append(strl())
    result = results(a, n, m)
    print(result)

if __name__ == '__main__':
    main()