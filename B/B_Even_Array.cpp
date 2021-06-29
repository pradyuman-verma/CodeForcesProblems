#include<bits/stdc++.h>

using namespace std;

#define int                  long long
#define mod                  1000000007
#define ps(x, y)             fixed << setprecision(y) << x
#define w(x)                 int x; cin >> x; while(x --)
#define mk(arr, n, type)     type *arr = new type[n];
#define gcd(x, y)            __gcd(x, y)
#define len(x)               int(x.size())
#define PI                   3.1415926535897932384626433832795
#define for0(i, n)           for (int i = 0; i < (int)(n); i ++) //0 based indexing
#define for1(i, n)           for (int i = 1; i <= (int)(n); i ++) // 1 based indexing
#define forc(i, l, r)        for (int i = (int)(l); i <= (int)(r); ++i) // l to r inclusive
#define forr0(i, n)          for (int i = (int)(n) - 1; i >= 0; --i) // reverse 0 based.
#define forr1(i, n)          for (int i = (int)(n); i >= 1; --i) // reverse 1 base
//short hand for usual tokens
#define pb                   push_back
#define fi                   first
#define se                   second
// to be used with algorithms that processes a container Eg: find(all(c),42)
#define all(x)               (x).begin(), (x).end() //Forward traversal
#define rall(x)              (x).rbegin, (x).rend() //reverse traversal
// shorthand for common types
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
//static_cast<new_type>(expression)
//swap(a,b)
//sort(a, a + n) sort(all(x))
void solve(){
    int n, cnte = 0, cnto = 0; cin >> n;
    mk(arr, n, int);
    for0(i, n){
        cin >> arr[i];
        if(i & 1){
            if(arr[i] % 2 == 0) cnte += 1;
        }
        else{
            if(arr[i] & 1) cnto += 1;
        }
    }
    if(cnte == cnto) cout << cnte << endl;
    else cout << -1 << endl;
}
signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    w(x) solve();
    return 0;
}
