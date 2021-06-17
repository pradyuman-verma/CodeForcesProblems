def ans(arr):
    cnt_A = arr.count('A')
    cnt_B =t - cnt_A
    if(cnt_A > cnt_B):
        return('Anton')
    elif(cnt_A < cnt_B):
        return('Danik')
    return('Friendship')

if __name__ == '__main__':
    t = int(input())
    n = list(input())
    print(ans(n))