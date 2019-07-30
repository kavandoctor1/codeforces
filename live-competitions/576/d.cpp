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
    int n;
    cin>>n;
    vector<int> money;
    For(n){
        int temp;
        cin>>temp;
        money.push_back(temp);
    }
    int t;
    cin>>t;
    For(t){
        int type;
        cin>>type;
        if(type==1){
            int a,b;
            cin>>a>>b;
            money[a-1] = b;
        }
        else{
            int x;
            cin>>x;
            For2(n){
                money[j] = max(money[j],x);
            }
        }
    }
    Forv(money){
        cout<<i<<" ";
    }
    cout<<"\n";
}