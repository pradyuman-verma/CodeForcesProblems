//pradyuman_verma
/* When you hit a roadblock, remember to rethink the solution ground up, not just try hacky fixes */
#include<bits/stdc++.h>
using namespace std;

#define int                  long long
#define mod                  1000000007
#define ps(x, y)             fixed << setprecision(y) << x
#define w(x)                 int x; cin >> x; while(x --)
#define gcd(x, y)            __gcd(x, y)
#define lcm(a,b)             ((a)*(b)) / gcd((a),(b))
#define endl                 "\n"
#define cel(x,a)             ((x + a - 1) / a)
#define print(x)             cout << (x ? "YES" : "NO") << endl
#define for0(i, n)           for (int i = 0; i < (int)(n); i ++) //0 based indexing
#define for1(i, n)           for (int i = 1; i <= (int)(n); i ++) // 1 based indexing
#define forr0(i, n)          for (int i = (int)(n) - 1; i >= 0; --i) // reverse 0 based.
#define forr1(i, n)          for (int i = (int)(n); i >= 1; --i) // reverse 1 base
#define debug(x)             cout << "debug : " << x << endl //debug tools
//short for common types
typedef vector<int> vi;
typedef pair<int, int> ii;
//short hand for usual tokens
#define pb                   push_back
#define fi                   first
#define se                   second
// to be used with algorithms that processes a container Eg: find(all(c),42)
#define all(x)               (x).begin(), (x).end() //Forward traversal
#define rall(x)              (x).rbegin(), (x).rend() //reverse traversal

// code here
class Solution{
    public :
        void Solve(){
            int n, k, x;
            cin >> n >> k;
            int s = 0;
            map<int, int> temp;
            for0(i, n){
                cin >> x;
                s += x / 10;
                if(x != 100){
                    int l = cel(x, 10)*10;
                    temp[l - x] += 1;
                    int m = (100 - l) / 10;
                    while(m --){
                        temp[10] += 1;
                    }
                }
            }
            for(auto xx : temp){
                if(xx.fi != 0){
                    // cout << xx.fi << " " << xx.se <<endl;
                    int j = min(xx.se, k / xx.fi);
                    k -= j * xx.fi;
                    s += j;
                    if(k == 0) break;
                }
            }  
            cout << s << endl;
        }
};

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    {
        Solution ob;
        ob.Solve();
    }
    return 0;
}

// 4 + 3 + 7 + 6 + 3 