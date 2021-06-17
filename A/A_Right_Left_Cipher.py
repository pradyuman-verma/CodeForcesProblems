def ans(arr):
    n = len(arr)
    s = ''
    if(n % 2):
        #left
        stop = n // 2 
        arr1 = arr[0 : stop] + [''] * n
        arr2 = arr[stop + 1 :][::-1] + [''] * n
        j, k = 0, 0
        for i in range(n - 1):
            if(i % 2 == 0):
                s += arr1[j]
                j += 1
            else:
                s += arr2[k]
                k += 1
        s += arr[stop]
        return(s[::-1])
    else: 
        stop = n // 2 - 1
        arr1 = arr[0 : stop] + [''] * n
        arr2 = arr[stop + 1 :][::-1] + [''] * n
        j, k = 0, 0
        for i in range(n - 1):
            if(i % 2 == 0):
                s += arr2[j]
                j += 1
            else:
                s += arr1[k]
                k += 1
        s += arr[stop]
        return(s[::-1])
if __name__ == '__main__':
    t = list(input())
    print(ans(t))