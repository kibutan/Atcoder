#include <bits/stdc++.h>
using namespace std;
int main() {
  int N=0,X,T=0;
  cin>>N>>X>>T;
  cout << (N/X) * T + (bool)(N%X) * T << endl;
}
