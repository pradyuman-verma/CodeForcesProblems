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
            int n;
            cin >> n;
            vi temp = PrimeFator(n);
            int a, b = 1, c = 1, n1 = temp.size();
            bool help = false;
            a = temp[0];
            int i = 1;
            while(i < n1){
                b *= temp[i];
                i += 1;
                if(b != a) break;
            }
            c = n / (a * b);
            if((a != b && b != c && c != a) && (c != 1)) help = true;
            print(help);
            if(help) cout << a << " " << b << " " << c << endl;
        }
        static vi PrimeFator(int x){
            vi temp;
            while(x % 2 == 0){
                temp.pb(2);
                x /= 2;
            }
            int i = 3;
            while(i * i <= x){
                while(x % i == 0){
                    temp.pb(i);
                    x /= i;
                }
                i += 2;
            }
            if(x > 2){
                temp.pb(x);
            }
            return(temp);
        } 
};

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    w(x){
        Solution ob;
        ob.Solve();
    }
    return 0;
}

// 4 + 3 + 7 + 6 + 3 