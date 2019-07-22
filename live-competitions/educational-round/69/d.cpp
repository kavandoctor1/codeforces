#include <bits/stdc++.h>
using namespace std;
#define For(x) for(int i = 0; i < x; i++)
#define For2(x) for(int j = 0; j < x; j++)
#define For3(x) for(int k = 0; k < x; k++)
#define Forv(vector) for(auto& i : vector)
#define Forv2(vector) for(auto& j : vector)
#define show(vector) for(auto& abcd : vector){cout<<abcd<<"\n";}
using ll = long long;

int main(){
    int n,m,k;
    cin>>n>>m>>k;
    int ls[n+1];
    ls[0]=0;
    For(n){     
        int temp;
        cin>>temp;
        ls[i+1] = ls[i]+temp;
    }
    int maxm = 0;
    For(n+1){
        for(int j = i;j<n+1;j++){
            int x = ls[j]-ls[i]-k*ceil((j-i+1.0)/m);
            maxm=max(maxm,x);
        }
    }
    cout<<maxm<<"\n";
}