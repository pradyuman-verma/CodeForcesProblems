def ans(arr):
    temp = set(arr)
    if(len(temp) % 2):
        return( "IGNORE HIM!" )
    return( "CHAT WITH HER!")

if __name__ == '__main__':
    s = list(input())
    print(ans(s))