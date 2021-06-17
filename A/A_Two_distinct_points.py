def ans(arr):
    l1, r1, l2, r2 = n[0], n[1], n[2], n[3]
    if(l1 < l2):
        return([l1, l2])
    else:
        return([l1 + 1, l2])
    
        
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = list(map(int, input().strip().split()))
        print(*ans(n))