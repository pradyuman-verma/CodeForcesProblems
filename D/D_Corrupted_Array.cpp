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
#define _debug(x)             cout << (#x) << "-> " << (x) << endl
#define print(x)             cout << (x ? "YES" : "NO") << endl
#define for0(i, n)           for (int i = 0; i < (int)(n); i ++) //0 based indexing
#define for1(i, n)           for (int i = 1; i <= (int)(n); i ++) // 1 based indexing
#define forr0(i, n)          for (int i = (int)(n) - 1; i >= 0; --i) // reverse 0 based.
#define forr1(i, n)          for (int i = (int)(n); i >= 1; --i) // reverse 1 base
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
struct number_iterator : iterator<random_access_iterator_tag, T>{
	T v;
	number_iterator(T _v) : v(_v) {}
	operator T&(){return v;}
	T operator *() const {return v;}
};
template <typename T>
struct number_range {
	T b,e;
	number_range(T b, T e):b(b),e(e){}
	number_iterator<T> begin(){return b;}
	number_iterator<T> end(){return e;}
};
/* make_pair like functions for our range type */
template<typename T> number_range<T> range(T e) {return number_range<T>(0, e);}
// inclusive range
template<typename T> number_range<T> range(T b, T e) {return number_range<T>(b, e);}
template<typename T>
void debug(vector<T> v){
    cout << "[ " ;
    for(int i = 0; i < v.size(); i ++) cout << v[i] << (i + 1 == v.size() ? "" : ", ");
    cout << " ]" << endl;
}
template<typename T>
void debug(T a[], int n){
    cout << "[ ";
    for(int i = 0; i < n; i ++) cout << a[i] << (i + 1 == n ? "" : ", ");
    cout << " ]" << endl;
}
template<typename T>
void debug(set<T> s){
    cout << "[ ";
    for(auto i = s.begin(); i != s.end();) cout << *i << (++i == s.end() ? "" : ", ");
    cout <<" ]" << endl;
}
template<typename T1, typename T2>
void debug(map<T1, T2> mp){
    for(auto i : mp) cout << "[ " << i.first << " : " << i.second << " ]" << endl;
}

// code here
class Solution{
    public :
        void Solve(){
            int n, s = 0, a, c, p, s2 = 0;
            cin >> n;
            int b[n + 2];
            bool help = false;
            for0(i, n + 2){
                cin >> b[i];
                s += b[i];
            }
            sort(b, b + n + 2);
            s2 = b[n + 1];
            p = Fx(b, n + 1, s - 2 * s2);
            if(p == -1){
                s2 = b[n];
                if(b[n + 1] == s - 2 * s2) a = n + 1, c = n;
                else{
                    cout << -1 << endl;
                    return;
                }
            }else{
                a = p;
                c = n + 1;
            }
            b[a] = b[c] = -1;
            for(auto x : b) if(x != -1) cout << x << " ";
            cout << endl;
        }
        static int Fx(int b[], int n, int x){
            for0(i, n) if(b[i] == x) return(i);
            return(-1);
        }
};

signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    Solution ob;
    w(x){
        ob.Solve();
    }
    return 0;
}

// More template
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
// 4 + 3 + 7 + 6 + 3 
// max = numeric_limits<int>::max(), min = numeric_limits<int>::min();