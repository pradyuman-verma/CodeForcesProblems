def ans(arr):
    arr.sort()
    return(min(arr[-2] - arr[0], arr[-1] - arr[1]))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(ans(a))