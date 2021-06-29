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
            int h, m;
            string s;
            cin >> h >> m >> s;
            int hh, mm;
            hh = stoi(s.substr(0, 2));
            mm = stoi(s.substr(3, 2));
            while(!ans(hh, mm, h, m)){
                mm = (mm + 1) % m;
                if(mm == 0) hh = (hh + 1) % h;
            }
            cout << hh / 10 << hh % 10 << ':' << mm / 10 << mm % 10 << endl;
        }
        static int stoi(string str){
            int ans = 0;
            int n = str.length();
            for0(i, n){
                if(isdigit(str[i])){
                    ans = ans * 10 + (str[i] - '0');
                }else return(-1);
            }
            return(ans);
        }
        static bool ans(int hh, int mm, int h, int m){
            int temp[10] = {0, 1, 5, -1, -1, 2, -1, -1, 8, -1};
            if(temp[hh % 10] == -1 || temp[hh / 10] == -1 || temp[mm % 10] == -1 || temp[mm / 10] == -1){
                return(false);
            }
            return((temp[mm % 10] * 10 + temp[mm / 10] < h) && (temp[hh % 10] * 10 + temp[hh / 10] < m));
        }
};

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    Solution ob;
    w(x) ob.Solve();
    return 0;
}

// 4 + 3 + 7 + 6 + 3 