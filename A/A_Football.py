from collections import Counter
def ans(arr):
    dummy = Counter(arr)
    max_ = max(list(dummy.values()))
    for i in dummy.keys():
        if(dummy[i] == max_):
            return(i)

if __name__ == '__main__':
    n = int(input())
    temp = []
    for _ in range(n):
        temp.append(input())
    print(ans(temp))