#include <bits/stdc++.h>
using namespace std;

bool check(vector<int> a, int find1, int find2) {
    
    bool ans = false;
    
    for(int i = 0; i < a.size(); ++i) {
        
        if(a[i] <= find1 && a[i]>= find2) {
            
            ans = true;
            break;
        }
    }
    return ans;
}

int main() {
    
    long long t;
    
    cin>>t;
    
    long long tc = 1;
    
    while(t--) {
        
        long long n;
        
        cin>>n;
        
        char in[n], out[n];
        
        vector<int> a_in, a_out;
        
        for(int i = 0; i < n; ++i) {
            
            cin>>in[i];
            
            if(in[i] == 'N') {
                
                a_in.push_back(i);
            }
        }
        for(int i = 0; i < n; ++i) {
             
            cin>>out[i];
            
            if(out[i] == 'N') {
                
                a_out.push_back(i);
            }
        }
        
        char ans[n][n];
        
        for(int i = 0; i < n; ++i) {
            
            for(int j = 0; j < n; ++j) {
            
                if(i == j) {
                    
                    ans[i][j] = 'Y';
                }
                else {
                    
                    if(i < j) {
                        
                        if(check(a_in, j, i+1) || check(a_out, j-1, i)) {
                            
                            ans[i][j] = 'N';
                        }
                        else {
                            
                            ans[i][j] = 'Y';
                        }
                    }
                    else {
                        
                        if(check(a_in, i-1, j) || check(a_out, i, j+1)) {
                            
                            ans[i][j] = 'N';
                        }
                        else {
                            
                            ans[i][j] = 'Y';
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<tc<<":\n";
        for(int i = 0; i < n; ++i) {
            
            for(int j = 0; j < n; ++j) {
                
                cout<<ans[i][j];
            }
            cout<<"\n";
        }
        tc++;
    }
    
	return 0;
}