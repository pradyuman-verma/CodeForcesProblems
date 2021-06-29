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
// standard template
template<typename T>
inline T Max(const T a, const T b){
	return a < b ? b : a;
}
template<typename T, typename ...Args>
T Max(const T a, const Args ...args){
	return Max(a, Max(args...));
}
template<typename T>
inline T Min(const T a, const T b){
	return a < b ? a : b;
}
template<typename T, typename ...Args>
T Min(const T a, const Args ...args){
	return Min(a, Min(args...));
}
template<typename T> 
inline T LCM(const T a, const T b){
    return lcm(a, b);
}
template<typename T, typename ...Args>
T LCM(const T a, const Args ...args) {
    return LCM(a, LCM(args ...));
}
// code here
class Solution{
    public :
        void Solve(){
            int n, m; cin >> n >> m;
            cout << nCr(n + 2 * m - 1, 2 * m);
        }
        static int Fact(int n){
            int factorial = 1;
            for(int i = 2; i <= n; i ++){
                factorial *= i;
                factorial = factorial % mod;
            }
            return(factorial);
        }
        static int nCr(int n, int r){
            r = (r > n - r) ? n - r : r;
            int ncr = Fact(n);
            ncr = (ncr * power(Fact(r), mod - 2, mod)) % mod;
            ncr = (ncr * power(Fact(n - r), mod - 2, mod)) % mod;
            return(ncr);
        }
        static int power(int x, int y, int p){
            int res = 1;
            x = x % p;
            if (x == 0) return 0;
            while (y > 0){
                if ((y & 1) != 0)
                    res = (res * x) % p;
                y = y >> 1; 
                x = (x * x) % p;
            }
            return res;
        }
};

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    Solution ob;
    {
        ob.Solve();
    }
    return 0;
}

// 4 + 3 + 7 + 6 + 3 