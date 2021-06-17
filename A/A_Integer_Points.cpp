#include<bits/stdc++.h>
#define int long long
using namespace std;

//__gcd(A,B)
//static_cast<new_type>(expression)
//swap(a,b)
//sort(a, a + n)

void solve(){
    int n, m, i, j;
    int e1 = 0, e2 = 0, o1 = 0, o2 = 0;
    cin >> n;
    for(i = 0; i < n; i ++){
        int p;
        cin >> p;
        if(p & 1){
            o1 += 1;
        }
        else{
            e1 += 1;
        }
    }
    cin >> m;
    for(j = 0; j < m; j ++){
        int q;
        cin >> q;
        if(q & 1){
            o2 += 1;
        }
        else{
            e2 += 1;
        }
    }
    cout << (e1 * e2) + (o1 * o2) << "\n"; 
}

signed main()
{
   int t;
   cin >> t;
   while(t --){
        solve();
   }
   return 0;
}
