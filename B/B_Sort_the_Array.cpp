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
#define print(x)             cout << (x ? "yes" : "no") << endl
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
            int n, cnt = 0;
            cin >> n;
            int arr[n + 1], temp[n];
            vi dmp;
            for0(i, n){
                cin >> arr[i];
                temp[i] = arr[i];
            }
            sort(temp, temp + n);
            arr[n] = 1e9;
            int i = 0;
            while(i < n){
                if(arr[i + 1] < arr[i]){
                    int j = i;
                    while(j < n && arr[j + 1] < arr[j]) j += 1;
                    cnt += 1;
                    if(cnt > 1){
                        break;
                    }
                    dmp.pb(i);
                    dmp.pb(j);
                    i = j;
                }
                i += 1;
            }
            if(cnt > 1){
                cout << "no";
            }else if(cnt == 0){
                cout << "yes" << endl;
                cout << 1 << " " << 1;
            }else{
                bool help = true;
                reverse(arr + dmp[0], arr + dmp[1] + 1);
                for0(i, n){
                    if(temp[i] != arr[i]){
                        help = false;
                        break;
                    }
                }
                print(help);
                if(help){
                    cout << dmp[0] + 1 << " " << dmp[1] + 1;
                }
            }
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