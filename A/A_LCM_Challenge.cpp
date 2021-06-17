#include<bits/stdc++.h>
#define int long long
using namespace std;

//static_cast<new_type>(expression)
// void swap(int a, int b){
//     a ^= b; 
//     b ^= a; 
//     a ^= b;
// }

signed main()
{
   int n;
   int64_t ans;
   cin >> n;
   if(n == 1){
       cout << 1;
   }
   else if(n == 2){
       cout << 2;
   }
   else{
       if(n % 2){
           ans = n * (n - 1) * (n - 2);
       }
       else if(n % 3 == 0){
           ans = (n - 1) * (n - 2) * (n - 3);
       }
       else{
           ans = n * (n - 1) * (n - 3);
       }
        cout << ans;
   }
   return 0;
}
