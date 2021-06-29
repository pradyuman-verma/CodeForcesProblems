def ans(arr, q):
    return(sum_ - arr[q - 1]) 

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    m = int(input())
    q = list(map(int, input().strip().split()))
    sum_ = sum(a)
    a.sort(reverse = True)
    for i in range(m):
        print(ans(a, q[i]))