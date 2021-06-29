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
    int n;
    string floor;
    cin >> n;
    cin >> floor;
    if(floor[0] == '1' || floor[n - 1] == '1'){
        cout << (2 * n) << endl;
    }
    else{
        int tmp;
        bool loop = true;
        int cnt1 = -1, cnt2 = -1 ;
        for0(i, n){
            if(floor[i] == '1' && loop){
                cnt1 = i;
                loop = false;
            }
            if(floor[i] == '1'){
                cnt2 = i;
            }
        }
        if(cnt1 == -1){
            cout << n << endl;
        }
        else{
            cout << max((n - cnt1) * 2, (cnt2 + 1) * 2) << endl;
        }
    }
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
