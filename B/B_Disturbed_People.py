n = int(input())
arr = list(map(int, input().strip().split()))
k = 0
i = 1
while i < n - 1:
    if(arr[i] == 0):
        if(arr[i - 1] == arr[i + 1] == 1):
            k += 1
            arr[i + 1] = 0
    i += 1
print(k)
