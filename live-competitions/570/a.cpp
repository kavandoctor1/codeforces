#include <bits/stdc++.h>
using namespace std;
#define For(x) for(int i = 0; i < x; i++)
#define For2(x) for(int j = 0; j < x; j++)
#define For3(x) for(int k = 0; k < x; k++)
#define Forv(vector) for(auto& i : vector)
#define Forv2(vector) for(auto& j : vector)
#define show(vector) for(auto& abcd : vector){cout<<abcd.first<<" "<<abcd.second<<"\n";}

bool interesting(int n){
    int sum = 0;
    while(n > 0){
        sum+=n%10;
        n=n/10;
    }
    if(sum%4 == 0){
        return true;
    }
    return false;
}

int main(){
    int n;
    cin>>n;
    while(true){
        if(interesting(n)){
            break;
        }
        n+=1;
    }
    cout<<n<<"\n";
}