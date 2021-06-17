#include<bits/stdc++.h>
#define int long long
using namespace std;

// void swap(int a, int b){
//     a ^= b; 
//     b ^= a; 
//     a ^= b;
// }

signed main()
{
   int n, k, p;
   cin>>n>>k;
    p = (k + n - 1) / n;
    cout<<p;
    return 0;
}
