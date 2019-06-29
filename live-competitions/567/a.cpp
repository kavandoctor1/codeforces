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
    ll x,y,z;
    cin>>x>>y>>z;
    ll a = x/z;
    ll b = y/z;
    ll total = a+b;
    ll xm = x%z;
    ll ym = y%z;
    ll moves = 0;
    if(xm+ym >= z){
        total++;
        moves = z-max(xm,ym);
    }
    cout<<total<<" "<<moves<<"\n";
}