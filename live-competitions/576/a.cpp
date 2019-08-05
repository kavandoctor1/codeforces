#include <bits/stdc++.h>
using namespace std;
#define For(x) for(int i = 0; i < x; i++)
#define For2(x) for(int j = 0; j < x; j++)
#define For3(x) for(int k = 0; k < x; k++)
#define Forv(vector) for(auto& i : vector)
#define Forv2(vector) for(auto& j : vector)
#define show(vector) for(auto& abcd : vector){cout<<abcd<<"\n";}
    
int main(){
    int n,x,y;
    cin>>n>>x>>y;
    int days[n+1];
    For(n){
        int temp;
        cin>>temp;
        days[i]=temp;
    }
    For(n){
        int m = days[i];
        bool ans = true;
        for(int j = max(i-x,0); j<i;j++){
            if(m>= days[j]){
                ans=false;
            }
        }
        for(int j = i+1; j < min(i+y+1,n); j++){
            if(m>=days[j]){
                ans=false;
            }
        }
        if(ans){
            cout<<i+1<<"\n";
            return 0;
        }
    }
}