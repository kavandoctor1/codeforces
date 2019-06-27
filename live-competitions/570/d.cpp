#include <bits/stdc++.h>
using namespace std;
#define For(x) for(int i = 0; i < x; i++)
#define For2(x) for(int j = 0; j < x; j++)
#define For3(x) for(int k = 0; k < x; k++)
#define Forv(vector) for(auto& b : vector)
#define Forv2(vector) for(auto& j : vector)
#define show(vector) for(auto& abcd : vector){cout<<abcd<<"\n";}
#define maxv(vector) *max_element(vector.begin(),vector.end())

int main(){
    int n;
    cin>>n;
    For3(n){
        int m;
        cin>>m;
        vector<int> candy;
        For2(m){
            int temp;
            cin>>temp;
            candy.push_back(temp);
        }
        int box[m+1];
        For(m+1){
            box[i] = 0;
        }
        Forv(candy){
            box[b]+=1;
        }
        vector<int> vec;
        For2(m+1){
            if(box[j]>0){
                vec.push_back(box[j]);
            }
        }
        sort(vec.begin(), vec.end());
	    reverse(vec.begin(), vec.end());
	    //show(vec);
	    int i = 0;
	    int sum = 0;
	    int current = vec[0]+1;
	    while(i<vec.size()){
	        if(current==1){
	            break;
	        }
	        if(vec[i]>=current){
	            sum+=current-1;
	            current--;
	        }
	        else{
	            sum+=vec[i];
	            current=vec[i];
	        }
	        i+=1;
	    }
	    cout<<sum<<"\n";
    }
    
}