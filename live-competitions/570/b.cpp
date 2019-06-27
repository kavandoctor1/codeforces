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
        int n,k;
        cin>>n>>k;
        vector<int> array;
        For(n){
            int temp;
            cin>>temp;
            array.push_back(temp);
        }
        if(*max_element(array.begin(),array.end())- *min_element(array.begin(), array.end())>2*k){
            cout<<"-1\n";
        }
        else{
            cout<<*min_element(array.begin(),array.end())+k<<"\n";
        }
        
    }
    
}