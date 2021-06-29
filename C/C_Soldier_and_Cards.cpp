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
#define for0(i, n)           for (auto i : range(n)) //0 based indexing
#define for1(i, n)           for (auto i : range(1ll, n + 1ll)) // 1 based indexing
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
#define present(c, e)        (c.find(e) != c.end())
#define cpresent(c, e)       (find(all(c), e) != c.end())
#define tr(c, it)             for(__typeof__((c)).begin() it = (c).begin(); it != (c).end(); it ++)
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
//debugging template
template<typename T>
void debug(vector<T> v){
    cout << "{" ;
    for(auto i : range(v.size())) cout << v[i] << (i + 1 == v.size() ? "" : ", ");
    cout << "}" << endl;
}
template<typename T, typename S>
void debug(pair<T, S> &p){
    cout << "(";
    cout << p.fi << ", " << p.se;
    cout << ")";
}
template<typename T, typename S>
void debug(vector<pair<T, S>> vp){
    cout << "{" ;
    for(auto i : range(vp.size())){debug(vp[i]);cout << (i + 1 == vp.size() ? "" : ", ");}
    cout << "}" << endl;
}
template<typename T>
void debug(vector<vector<T>> vv){
    cout << "[" ;
    for(auto i : range(vv.size())) debug(vv[i]);
    cout << "]" << endl;
}
template<typename T>
void debug(T a[], int n){
    cout << "{";
    for(auto i : range(n)) cout << a[i] << (i + 1 == n ? "" : ", ");
    cout << "}" << endl;
}
template<typename T>
void debug(set<T> s){
    cout << "{";
    for(auto i = s.begin(); i != s.end();) cout << *i << (++i == s.end() ? "" : ", ");
    cout <<"}" << endl;
}
template<typename T>
void debug(multiset<T> s){
    cout << "{";
    for(auto i = s.begin(); i != s.end();) cout << *i << (++i == s.end() ? "" : ", ");
    cout <<"}" << endl;
}
template<typename T1, typename T2>
void debug(map<T1, T2> mp){
    cout << "{";
    for(auto i = mp.begin(); i != mp.end();) cout << "(" << i->first << " : " << i->second << ")" << (++i == mp.end() ? "": ",");
    cout << "}" << endl;
}

// code here
class Solution{
    public :
        void Solve(){
            int n, x, k1, k2;
            cin >> n;
            queue<int> p1, p2;
            cin >> k1;
            for0(i, k1){
                cin >> x;
                p1.push(x);
            }
            cin >> k2;
            for0(i, k2){
                cin >> x;
                p2.push(x);
            }
            int cnt = 0;
            while(!p1.empty() && !p2.empty()){
                if(p1.front() > p2.front()){
                    p1.push(p2.front());
                    p2.pop();
                    p1.push(p1.front());
                    p1.pop();
                }else if(p1.front() < p2.front()){
                    p2.push(p1.front());
                    p1.pop();
                    p2.push(p2.front());
                    p2.pop();
                }else{
                    p2.push(p2.front());
                    p2.pop();
                    p1.push(p1.front());
                    p1.pop();
                }
                cnt += 1;
                if(cnt > 1e5){
                    cnt = -1;
                    break;
                }
            }
            cout << cnt << " ";
            if(p1.empty()) cout << 2;
            else if(p2.empty()) cout << 1;
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
template<typename T>
int Modulo(T x, T N){
    return (x % N + N) % N;
}
// motivation 101 :
// THOSE WHO CANN'T REMEMBER THE PAST ARE CONDEMNED TO REPEAT IT -- DYNAMIC PROGRAMMING.
// 4 + 3 + 7 + 6 + 3 
// max = numeric_limits<int>::max(), min = numeric_limits<int>::min();