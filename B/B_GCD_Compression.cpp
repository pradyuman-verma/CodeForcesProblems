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
const int N = 2e5 + 5;

void solve(){
    int n, a[N];
    cin >> n;
    vector<int> even, odd;
    for(int i = 1; i <= 2 * n; i ++){
        cin >> a[i];
        if(a[i] & 1){
            odd.push_back(i);
        }
        else{
            even.push_back(i);
        } 
    }
    vector <pair< int, int >> ans;
    int x = even.size(), y = odd.size();
    for(int i = 0; i + 1 < x; i += 2){
        ans.push_back({even[i], even[i + 1]});
    }
    for(int i = 0; i + 1 < y; i += 2){
        ans.push_back({odd[i], odd[i + 1]});
    }
    for0(i, n - 1){
        cout << ans[i].first << " " << ans[i].second << endl; 
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
