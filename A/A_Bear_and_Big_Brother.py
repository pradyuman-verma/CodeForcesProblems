def ans(arr):
    a, b = arr[0], arr[1]
    cnt = 0
    while a <= b:
        a *= 3
        b *= 2
        cnt += 1
    return cnt

if __name__ == '__main__':
    ab = list(map(int, input().strip().split()))    
    #a = limak, b = bob
    print(ans(ab))