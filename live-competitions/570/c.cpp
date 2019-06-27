#include <bits/stdc++.h>
using namespace std;
#define For(x) for(int i = 0; i < x; i++)
#define For2(x) for(int j = 0; j < x; j++)
#define For3(x) for(int k = 0; k < x; k++)
#define Forv(vector) for(auto& i : vector)
#define Forv2(vector) for(auto& j : vector)
#define show(vector) for(auto& abcd : vector){cout<<abcd.first<<" "<<abcd.second<<"\n";}

int main(){
    int n;
    cin>>n;
    For(n){
        long long k,n,a,b;
        cin>>k>>n>>a>>b;
        if(k<=b*n){
            cout<<"-1\n";
        }
        else{
            long long left = k-n*b-1;
            long long answer = min(left/(a-b), n);
            cout<<answer<<"\n";
        }
    }
    
    
}