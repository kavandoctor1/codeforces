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
    For(n){
        int m;
        cin>>m;
        vector<int> vect;
        For2(m){
            int temp;
            cin>>temp;
            vect.push_back(temp);
        }
        sort(vect.begin(),vect.end());
        reverse(vect.begin(),vect.end());
        if(vect.size()<3){
            cout<<"0\n";
        }
        else{
            int k = min(vect[1]-1,(int)(vect.size()-2));
            cout<<max(0,k)<<"\n";
        }
    }
}