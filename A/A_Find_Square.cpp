#include<bits/stdc++.h>
#define int long long
using namespace std;

// void swap(int a, int b){
//     a ^= b; 
//     b ^= a; 
//     a ^= b;
// }

void black(int i, int j, string z[], int n, int m){
    int x, y;
    for(y = j; y < m; y ++){
        if(z[i][y] != 'B'){
            y -= 1;
            break;
        }
    }
    for(x = i; x < n; x ++){
        if(z[x][j] != 'B'){
            x -= 1;
            break;
        }
    }
    x = x - i;
    y = y - j;
    x = floor(x / 2) + i + 1;
    y = floor(y / 2) + j + 1;
    cout << x << " " << y << endl;
}
signed main(){
   int n, m, i;
   cin >> n >> m;
   string a[n];
    for(i = 0; i < n; i ++){
        cin >> a[i];
    }
    char loop = false;
    for(i = 0; i < n; i ++){
        for(int j = 0; j < m; j ++){
            if(a[i][j] == 'B'){
                black(i, j, a, n, m);
                loop = true;
                break;
            }
        }
        if(loop){
                break;
            }
    }
}
