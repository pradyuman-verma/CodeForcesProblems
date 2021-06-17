#include<bits/stdc++.h>
#define int long long
using namespace std;

// void swap(int a, int b){
//     a ^= b; 
//     b ^= a; 
//     a ^= b;
// }
void solve(){
    int n;
    string s;
    char ans = true;
    cin >> n;
    cin >> s;
    for(int i = 0; i < floor(n / 2); i ++){
        if(s[i] == s[n - (i + 1)]){
            //cout << s[i] <<" "<< s[n - (i + 1)] << endl;
            continue;
        }
        else{
            if (abs((int)s[i] - (int)s[n - (i + 1)]) == 2){
                continue;
            }
            else{
                ans = false;
                cout << "NO" << endl;
                break;
            }
        }   
    }
    if(ans){
        cout << "YES" << endl;
    }
}

signed main()
{
   int t, n, i, a[n];
   cin >> t;
   while(t --){
        solve();
   }
   return 0 ;
}
