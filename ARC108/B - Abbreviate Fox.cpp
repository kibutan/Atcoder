#include<iostream>
#include<string>
using namespace std;
 
int main(){
  int N;
  string s,t;
  cin >> N;
  cin >> s;
  for(int i = 0; i < s.size(); i++){
//    cout <<"s[i]" << s[i]<<endl;
    t += s[i];
//	cout << t;
    if(t.find("fox") != std::string::npos){
      t.erase(t.end()-1);
      t.erase(t.end()-1);
      t.erase(t.end()-1);      
    }else{
//      cout<<t<<endl;
    }
  }
  cout << t.size();
  return 0;
}
