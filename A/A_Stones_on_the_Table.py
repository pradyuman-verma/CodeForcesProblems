def ans(arr):
    cnt = 0
    i = 0
    while i < n - 1:
        if(arr[i] == arr[i + 1]):
            cnt += 1
        i += 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    s = list(input())
    print(ans(s))