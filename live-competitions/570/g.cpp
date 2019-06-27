#include <bits/stdc++.h>
using namespace std;
#define For(x) for(int i = 0; i < x; i++)
#define For2(x) for(int j = 0; j < x; j++)
#define For3(x) for(int k = 0; k < x; k++)
#define Forv(vector) for(auto& b : vector)
#define Forv2(vector) for(auto& j : vector)
#define show(vector) for(auto& abcd : vector) { cout<<abcd.first<<" "<<abcd.second<<"\n";}
#define maxv(vector) *max_element(vector.begin(),vector.end())

int main(){
    int n;
    cin>>n;
    For3(n){
        int m;
        cin>>m;
        vector<pair<int, int> > candy;
        For2(m){
            int t,s;
            cin>>t>>s;
            pair<int,int> p(t,s);
            candy.push_back(p);
        }
        vector<pair<int, int> > vec;
        For(m+1){
            pair<int,int> p(0,0);
            vec.push_back(p);
        }
        Forv(candy){
            vec[b.first].first+=1;
            vec[b.first].second+=b.second;
        }
        sort(vec.begin(), vec.end());
	    reverse(vec.begin(), vec.end());
	    cout<<"vector:\n";
	    show(vec);
	    int i = 0;
	    int sum = 0;
	    int fsum = 0;
	    int current = vec[0].first+1;
	    while(i<vec.size()){
	        if(current==1){
	            break;
	        }
	        if(vec[i].first>=current){
	            sum+=current-1;
	            current--;
	            fsum+=min(current, vec[i].second);
	        }
	        else{
	            sum+=vec[i].first;
	            current=vec[i].first;
	            fsum+=vec[i].second;
	        }
	        i+=1;
	    }
	    cout<<sum<<" "<<fsum<<"\n";
    }
    
}