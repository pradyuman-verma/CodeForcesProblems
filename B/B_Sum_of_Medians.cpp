/******************************************/
/*    AUTHOR:         PRADYUMAN VERMA     */
/*    INSTITUITION:   IIT ROORKEE         */
/******************************************/
/* When you hit a roadblock, remember to rethink the solution ground up, not just try hacky fixes */
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
typedef map<int, int> mpp;
/* map is like dict in python.
use pair not map, it can be sort easily
static_cast<new_type>(expression)
swap(a,b)
sort(a, a + n) sort(all(x)) */
void solve(){
    int n, k; cin >> n >> k;
    int m = n / 2;
    m += 1;
    int temp[n * k];
    int j = 0;
    for0(i, n * k){
        cin >> temp[i];
    }
    int sum = 0;
    j = k;
    for(int i = n * k - m; j > 0; i -= m){
        sum += temp[i];
        j -= 1;
    }
    cout << sum << endl;
}

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    w(x) solve();
    return 0;
}