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
   int n, i;
   cin >> n;
   int a[n];
   char ans = false;
   for(i = 0; i < n; i ++){
       cin >> a[i];
        if(a[i] == 1){
            ans = true;
        }
   }
   if(ans){
       cout << "HARD";
   }
   else{
       cout << "EASY";
   }
}
