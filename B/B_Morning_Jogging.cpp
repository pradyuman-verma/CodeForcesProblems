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
typedef vector<ii> vii;
typedef map<int, int> mpp;
//short hand for usual tokens
#define pb                   push_back
#define fi                   first
#define se                   second
#define mp                   make_pair
// to be used with algorithms that processes a container Eg: find(all(c),42)
#define all(x)               (x).begin(), (x).end() //Forward traversal
#define rall(x)              (x).rbegin(), (x).rend() //reverse traversal

// code here
void solve(){
    int n, m, val;
    cin >> n >> m;
    multiset<pair<int, int>> tmp;
    vector<vi> arr(n, vi(m, 0));
    for0(i, n){
        for0(j, m){
            cin >> val;
            tmp.insert({val, i});
        }
    }
    for0(i, m){
        auto it = tmp.begin();
        arr[it->se][i] = it->first;
        tmp.erase(it);
    }
    while(!tmp.empty()){
        auto it = tmp.begin();  
        for0(i, m){
            if(arr[it->se][i] == 0){
                arr[it->se][i] = it->fi;
                tmp.erase(it);
                break;
            } 
        }
    }
    for0(i, n){
        for0(j, m){
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    w(x) solve();
    return 0;
}

/*  - map is like dict in python,
    - use pair not map, it can be sort easily, for(auto [key, value] : map)
    - static_cast<new_type>(expression),
    - swap(a,b),
    - sort(a, a + n) sort in ascending order,
    - sort(a, a + n, greater<int>()) to sort in descending order,
    - sort(all(x)), reverse(all(x))
    -  (about −9 · 10^18 ... 9 · 10^18) long long int
    - gcd(a, b) divides every linear combination of a, b i.e. as + bt 
    - cout << fixed << setprecision(12) aka ps(x, y)
    - to take input of a vector arr(n) use {for(auto &it : arr) cin >> it;}
    - unsigned long long int > signed long long int on +ve x axis
    - sort(all(v)); v.erase(unique(all(v)),end(v)); sort and remove duplicates.
    - (s1.find(s2) != string::npos) it checks if s2 is in s1 or not (The function returns the index of the first occurrence of sub-string).
    - s.subs(l, r) give substring from l to r;
    - memset(temp, value, size);
    - 4 + 3 + 7 + 6 + 3 */