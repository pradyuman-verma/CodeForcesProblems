#include<bits/stdc++.h>

using namespace std;

#define int                  long long
#define mod                  1000000007
#define ps(x, y)             fixed << setprecision(y) << x
#define w(x)                 int x; cin >> x; while(x --)
#define mk(arr, n, type)     type *arr = new type[n];
#define gcd(x, y)            __gcd(x, y)
#define pb                   push_back
#define length(v)            v.size()
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
    int n, r;
    cin >> n >> r;
    set<int> s;
    for0(i, n){
        int x; cin >> x;
        s.insert(x);
    }
    int ans = 0, index = 0;
    set<int>::reverse_iterator rit;
    for(rit = s.rbegin(); rit != s.rend(); rit++){
        if(*rit - index > 0){
            index += r;
            ans += 1;
        }
        else break;
    }
    cout << ans << endl;
}

signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
   w(x){
       solve();
   }
   return 0;
}
