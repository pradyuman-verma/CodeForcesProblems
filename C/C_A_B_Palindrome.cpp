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
            int a, b, n, cnt;
            string s;
            cin >> a >> b >> s;
            n = s.length();
            for0(j, 2){
                for(int i = 0; i < n; i ++){
                    if(s[i] != '?'){
                        if(s[n - (i + 1)] == '?')
                            s[n - (i + 1)] = s[i];
                        else if(s[i] != s[n - (i + 1)]){
                            out();
                            return;
                        }
                    }
                }
                reverse(all(s));
            }
            a -= count(all(s), '0');
            b -= count(all(s), '1');
            cnt = count(all(s), '?');
            bool help = (n & 1 && s[n / 2] == '?');
            if(a < 0 || b < 0 || a + b != cnt || (help && a % 2 == 0 && b % 2 == 0)){
                out();
                return;
            }
            if(a & 1 || b & 1){
                if(s[n / 2] != '?'){
                    out();
                    return;
                }
                s[n / 2] = (a & 1 ? '0' : '1');
                if(a & 1) a -= 1;
                else b -= 1;
            }
            if(a & 1 || b & 1){
                out();
                return;
            }
            for0(i, n){
                if(s[i] == '?'){
                    if(a > 0){
                        a -= 2;
                        s[i] = s[n - (i + 1)] = '0';
                    }else{
                        b -= 2;
                        s[i] = s[n - (i + 1)] = '1';
                    }
                }
            }
            cout << s << endl;
        }
        static void out(){
            cout << -1 << endl;
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