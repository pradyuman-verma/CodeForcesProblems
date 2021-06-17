#include<bits/stdc++.h>
#define int long long
using namespace std;

int cells(int w, int h){
    int pr;
    pr = 2 * (w + h) - 4;
    return(pr);
}

signed main()
{
   int w, h, k;
    cin >> w >> h >> k;
    int cnt = 0;
    while(k --){
        cnt += cells(w, h);
        w -= 4;
        h -= 4;
    }
    cout << cnt;
    return 0;
}
