#include <iostream>
#include "Median-of-Two-Sorted-Arrays.cpp"
using namespace std;




int main() {
  Solution s;
  int A[] = {1, 3, 5, 7, 7, 7, 9};
  int B[] = {4, 6, 6, 8};
  int C[] = {1};
  int D[] = {1};
  int k;
  cin >> k;
  cout << s.lbsearch(3, B, 4) << endl;
  cout << s.rbsearch(1, C, 1) << endl;
  cout << s.searchK(C, 1, D, 1, k) << endl; 
}











