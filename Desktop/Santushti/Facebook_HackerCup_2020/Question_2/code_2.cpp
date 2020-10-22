#include <bits/stdc++.h>
using namespace std;

int main() {
    
    long long t;
    
    cin>>t;
    
    long long tc = 1;
    
    while(t--) {
        
        string str;
        
        long long n;
        
        cin>>n;
        
        cin>>str;
        
        multiset<char> s(str.begin(), str.end());
        
        char ans = 'N';
        
        if(s.count('A') == s.count('B')+1 || s.count('B') == s.count('A')+1) {
            
            ans = 'Y';
        }
        
        cout<<"Case #"<<tc<<": "<<ans<<"\n";
        
        tc++;
    }
    
	return 0;
}