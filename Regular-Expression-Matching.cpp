#include <string.h>
#include <iostream>
using namespace std;

// not very efficient, we can cache results to improve the efficiency

class Solution {
public:
  bool isMatch(const char *s, const char *p) {
    if (strlen(s) == 0) {
      int len = strlen(p);
      if (len == 0) return true;
      if (len > 1) return p[1] == '*' && isMatch(s, p + 2);
      return false;
      }

    
    if (strlen(p) == 0)
      return false;

    if (strlen(p) == 1) {
      return strlen(s) == 1 && (s[0] == p[0] || p[0] == '.');
    }
    // now strlen(p) > 1
    if (p[1] == '*') {
      return isMatch(s, p + 2) || (p[0] == '.' || p[0] == s[0]) && isMatch(s + 1, p);
    }
    else { // p[1] != '*'
      return (p[0] == '.' || p[0] == s[0]) && isMatch(s + 1, p + 1);
    }

  }
};


int main() {
  Solution s;
  cout << s.isMatch("aa", "a*") << endl;
  return 0;
}





