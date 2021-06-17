def ans(arr, n):
    if(n % 2):
        x = n // 2
        print('YES')
        print(2)
        print('{} {}'.format(arr[0:x], arr[x:]))
    else:
        if(n == 2 and arr[0] >= arr[1]):
            print('NO')
        else:
            print('YES')
            print(2)
            print('{} {}'.format(arr[0], arr[1:]))
            
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        ans(s, n)