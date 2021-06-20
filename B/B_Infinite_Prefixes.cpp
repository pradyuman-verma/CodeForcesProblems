//pradyuman
/* When you hit a roadblock, remember to rethink the solution ground up, not just try hacky fixes */
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define mod 1000000007
#define ps(x, y) fixed << setprecision(y) << x
#define w(x)  \
    int x;    \
    cin >> x; \
    while (x--)
#define gcd(x, y) __gcd(x, y)
#define lcm(a, b) ((a) * (b)) / gcd((a), (b))
#define endl "\n"
#define cel(x, a) ((x + a - 1) / a)
#define _debug(x) cout << (#x) << "-> " << (x) << endl
#define deb(...) logger(#__VA_ARGS__, __VA_ARGS__)
#define print(x) cout << (x ? "YES" : "NO") << endl
#define for0(i, n) for (auto i : range(n))                //0 based indexing
#define for1(i, n) for (auto i : range(1ll, n + 1ll))     // 1 based indexing
#define forr0(i, n) for (int i = (int)(n)-1; i >= 0; --i) // reverse 0 based.
#define forr1(i, n) for (int i = (int)(n); i >= 1; --i)   // reverse 1 base
//short for common types
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef map<int, int> mpp;
//short hand for usual tokens
#define pb push_back
#define fi first
#define se second
#define mp make_pair
// to be used with algorithms that processes a container Eg: find(all(c),42)
#define all(x) (x).begin(), (x).end()    //Forward traversal
#define rall(x) (x).rbegin(), (x).rend() //reverse traversal
#define present(c, e) (c.find(e) != c.end())
#define cpresent(c, e) (find(all(c), e) != c.end())
#define tr(c, it) for (auto it : c)
// standard template
template <typename T>
struct number_iterator : iterator<random_access_iterator_tag, T>
{
    T v;
    number_iterator(T _v) : v(_v) {}
    operator T &() { return v; }
    T operator*() const { return v; }
};
template <typename T>
struct number_range
{
    T b, e;
    number_range(T b, T e) : b(b), e(e) {}
    number_iterator<T> begin() { return b; }
    number_iterator<T> end() { return e; }
};
/* make_pair like functions for our range type */
template <typename T>
number_range<T> range(T e) { return number_range<T>(0, e); }
template <typename T>
number_range<T> range(T b, T e) { return number_range<T>(b, e); }
//debugging template
template <typename... Args>
void logger(string vars, Args &&...values)
{
    cout << "[" << vars << "]"
         << " = ";
    string delim = "";
    cout << "[" << (..., (cout << delim << values, delim = ", ")) << "]" << endl;
}
template <typename T>
void debug(vector<T> v)
{
    cout << "{";
    for (auto i : range(v.size()))
        cout << v[i] << (i + 1 == v.size() ? "" : ", ");
    cout << "}" << endl;
}
template <typename T, typename S>
void debug(pair<T, S> &p)
{
    cout << "(";
    cout << p.fi << ", " << p.se;
    cout << ")";
}
template <typename T, typename S>
void debug(vector<pair<T, S>> vp)
{
    cout << "{";
    for (auto i : range(vp.size()))
    {
        debug(vp[i]);
        cout << (i + 1 == vp.size() ? "" : ", ");
    }
    cout << "}" << endl;
}
template <typename T>
void debug(vector<vector<T>> vv)
{
    cout << "[";
    for (auto i : range(vv.size()))
        debug(vv[i]);
    cout << "]" << endl;
}
template <typename T>
void debug(T a[], int n)
{
    cout << "{";
    for (auto i : range(n))
        cout << a[i] << (i + 1 == n ? "" : ", ");
    cout << "}" << endl;
}
template <typename T>
void debug(set<T> s)
{
    cout << "{";
    for (auto i = s.begin(); i != s.end();)
        cout << *i << (++i == s.end() ? "" : ", ");
    cout << "}" << endl;
}
template <typename T>
void debug(multiset<T> s)
{
    cout << "{";
    for (auto i = s.begin(); i != s.end();)
        cout << *i << (++i == s.end() ? "" : ", ");
    cout << "}" << endl;
}
template <typename T1, typename T2>
void debug(map<T1, T2> mp)
{
    cout << "{";
    for (auto i = mp.begin(); i != mp.end();)
        cout << "(" << i->first << " : " << i->second << ")" << (++i == mp.end() ? "" : ",");
    cout << "}" << endl;
}
// maths helper
int modExpo(int a, int b, int m = mod)
{
    int res = 1;
    while (b > 0)
    {
        if (b & 1)
            res = (res * a) % m;
        a = (a * a) % m;
        b = b >> 1;
    }
    return res;
}
void extendEuclids(int a, int b, int *v)
{
    if (b == 0)
    {
        v[0] = 1, v[1] = 0, v[2] = a;
        return;
    }
    extendEuclids(b, a % b, v);
    int x = v[1];
    v[1] = v[0] - v[1] * (a / b);
    v[0] = x;
    return;
} //pass an arry of size1 3
int modInv(int a, int b)
{
    int arr[3];
    extendEuclids(a, b, arr);
    return arr[0];
} //for non prime b
int modInv_lil(int a, int b)
{
    return modExpo(a, b - 2, b);
}
int add(int a, int b, int c = mod)
{
    int res = a + b;
    return (res >= c ? res - c : res);
}
int mod_mul(int a, int b, int c = mod)
{
    int res = a * b;
    return (res >= c ? res % c : res);
}
int mod_sub(int a, int b, int m = mod)
{
    a = a % m;
    b = b % m;
    return (((a - b) % m) + m) % m;
}
int mod_div(int a, int b, int m = mod)
{
    a = a % m;
    b = b % m;
    return (mod_mul(a, modInv_lil(b, m), m) + m) % m;
} //only for prime m
// code here
class Solution
{
public:
    void Solve()
    {
        int n, x, cnt = 0, l, p;
        string s;
        cin >> n >> x >> s;
        set<int> temp;
        int arr[n];
        for0(i, n){
            if (s[i] - '0')
                cnt -= 1;
            else
                cnt += 1;
            arr[i] = cnt;
        }
        l = cnt;
        cnt = count(arr, arr + n, x);
        if(l == 0 && cnt){
            cout << -1 << endl;
            return;
        }
        for0(i, n){
            p = x - arr[i];
            if(p == 0) temp.insert(i + 1);
            else if(l != 0 && p % l == 0 && (p / l) > 0) 
                temp.insert((p / l) * n + (i + 1));
        }
        cnt = (x == 0) ? temp.size() + 1 : temp.size();
        cout << cnt << endl;
    }
};

signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solution ob;
    w(x)
    {
        ob.Solve();
    }
    return 0;
}

// More template
template <typename T>
inline T Max(const T a, const T b)
{
    return a < b ? b : a;
}
template <typename T, typename... Args>
T Max(const T a, const Args... args)
{
    return Max(a, Max(args...));
}
template <typename T>
inline T Min(const T a, const T b)
{
    return a < b ? a : b;
}
template <typename T, typename... Args>
T Min(const T a, const Args... args)
{
    return Min(a, Min(args...));
}
template <typename T>
inline T LCM(const T a, const T b)
{
    return lcm(a, b);
}
template <typename T, typename... Args>
T LCM(const T a, const Args... args)
{
    return LCM(a, LCM(args...));
}
// motivation 101 :
// THOSE WHO CANN'T REMEMBER THE PAST ARE CONDEMNED TO REPEAT IT -- DYNAMIC PROGRAMMING.
// 4 + 3 + 7 + 6 + 3
// max = numeric_limits<int>::max(), min = numeric_limits<int>::min();