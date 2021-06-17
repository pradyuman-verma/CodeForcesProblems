def ans(arr):
    ans = arr + 1
    while len(set(str(ans))) != 4:
        ans += 1
    return ans

if __name__ == '__main__':
    t = int(input())
    print(ans(t))