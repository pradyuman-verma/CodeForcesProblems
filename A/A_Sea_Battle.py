def ans(w1, h1, w2, h2):
    cnt = 0
    if(w1 >= w2):
        cnt += (w1 + 2) * (h1 + 2) - (w1 * h1)
        h2 -= 1
        cnt += 3 + (h2 * 2)
    else: 
        cnt += (w2 + 2) * (h2 + 2) - (w2 * h2)
        h1 -= 1
        cnt += 3 + (h1 * 2)
    return cnt - 1

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(ans(arr[0], arr[1], arr[2], arr[3]))