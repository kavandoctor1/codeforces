#include <bits/stdc++.h>
using namespace std;
#define For(x) for(int i = 0; i < x; i++)
#define For2(x) for(int j = 0; j < x; j++)
#define For3(x) for(int k = 0; k < x; k++)
#define Forv(vector) for(auto& i : vector)
#define Forv2(vector) for(auto& j : vector)
#define show(vector) for(auto& abcd : vector){cout<<abcd<<" ";}
using ll = long long;

int main(){
    int n,k;
    cin>>n>>k;
    vector<int> ls;
    For(n){
        int temp;
        cin>>temp;
        ls.push_back(temp);
    }
    vector<int> diff;
    For(n-1){
        diff.push_back(ls[i+1]-ls[i]);
    }
    sort(diff.begin(),diff.end());
    reverse(diff.begin(),diff.end());
    int total = 0;
    For(k-1){
        total+=diff[i];
    }
    cout<<max(0,ls[n-1]-ls[0]-total)<<"\n";
}