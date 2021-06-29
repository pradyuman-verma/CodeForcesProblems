#include<bits/stdc++.h>

using namespace std;

#define int                  long long
#define mod                  1000000007
#define ps(x, y)             fixed << setprecision(y) << x
#define w(x)                 int x; cin >> x; while(x --)
#define mk(arr, n, type)     type *arr = new type[n];
#define gcd(x, y)            __gcd(x, y)
#define PI                   3.1415926535897932384626433832795
#define for0(i, n)           for (int i = 0; i < (int)(n); i ++) //0 based indexing
#define for1(i, n)           for (int i = 1; i <= (int)(n); i ++) // 1 based indexing
#define forc(i, l, r)        for (int i = (int)(l); i <= (int)(r); ++i) // l to r inclusive
#define forr0(i, n)          for (int i = (int)(n) - 1; i >= 0; --i) // reverse 0 based.
#define forr1(i, n)          for (int i = (int)(n); i >= 1; --i) // reverse 1 base
//static_cast<new_type>(expression)
//swap(a,b)
//sort(a, a + n)

void solve(){
    string s;
    cin >> s;
    int a, b = 1, c = 1, l = s.size();
    for0(i, l){
        if(s[i] == 'm' | s[i] == 'w'){
            cout << 0;
            exit(0);
        }
    }
    for0(i, l){
        if((s[i] == s[i + 1]) && (s[i] == 'n' || s[i] == 'u')){
            a = (b + c) % mod;
        }
        else{
            a = b;
        }
        c = b; 
        b = a;
    }
    cout << b;
}

signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
   //w(x){
    solve();
   //}
   return 0;
}
