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
#define lcm(a,b)             ((a)*(b)) / gcd((a),(b))
#define len(x)               int(x.size())
#define PI                   3.1415926535897932384626433832795
#define endl                 "\n"
#define print(x)             cout << (x ? "YES" : "NO") << endl
#define for0(i, n)           for (int i = 0; i < (int)(n); i ++) //0 based indexing
#define for1(i, n)           for (int i = 1; i <= (int)(n); i ++) // 1 based indexing
#define forc(i, l, r)        for (int i = (int)(l); i <= (int)(r); ++i) // l to r inclusive
#define forr0(i, n)          for (int i = (int)(n) - 1; i >= 0; --i) // reverse 0 based.
#define forr1(i, n)          for (int i = (int)(n); i >= 1; --i) // reverse 1 base
//short hand for usual tokens
#define pb                   push_back
#define fi                   first
#define se                   second
#define mp                   make_pair
// to be used with algorithms that processes a container Eg: find(all(c),42)
#define all(x)               (x).begin(), (x).end() //Forward traversal
#define rall(x)              (x).rbegin(), (x).rend() //reverse traversal
// shorthand for common types
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef map<int, int> mpp;
/* Code Here */
void solve(){
    int n, mx = 0; cin >> n;
    int arr[n];
    for0(i, n){
        cin >> arr[i];
    }
    int i = 0;
    while(i < n){
        int j = i + 1;
        int cnt = 1;
        while(j < n){
            if(arr[j] <= arr[j - 1]){
                break;
            }
            cnt += 1;
            j += 1;
        }
        mx = max(cnt, mx);
        i = j;
    }
    cout << mx ;
}

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    solve();
    return 0;
}

/*  - map is like dict in python,
    - use pair not map, it can be sort easily, for(auto [key, value] : map)
    - static_cast<new_type>(expression),
    - swap(a,b),
    - sort(a, a + n) sort in ascending order,
    - sort(a, a + n, greater<int>()) to sort in descending order,
    - sort(all(x)),
    - gcd(a, b) divides every linear combination of a, b i.e. as + bt 
    - cout << fixed << setprecision(12) aka ps(x, y)
    - to take input of a vector arr(n) use {for(auto &it : arr) cin >> it;}
    - unsigned long long int > signed long long int on +ve x axis
    - 
    - 4 + 3 + 7 + 6 + 3 */