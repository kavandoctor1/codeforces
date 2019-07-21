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
    int total = 0;
    vector<int> seats;
    For(n){
        int temp;
        cin>>temp;
        total+=temp;
        seats.push_back(temp);
    }
    int team = seats[0];
    vector<int> index;
    index.push_back(1);
    int ind = 1;
    Forv(seats){
        if(seats[0]>=2*i){
            team+=i;
            index.push_back(ind);
        }
        ind+=1;
    }
    if(2*team>total){
        cout<<index.size()<<"\n";
        Forv(index){
            cout<<i<<" ";
        }
        cout<<"\n";
    }
    else{
        cout<<"0\n";
    }
}