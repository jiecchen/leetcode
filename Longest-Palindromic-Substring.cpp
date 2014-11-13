class Solution {
public:
  string longestPalindrome(string s) {
    int maxLength = 1;
    int re_i = 0;
    for (int i = 0; i < s.length(); i++) {
      int len = 0;
      while (i - len >= 0 && i + len < s.length() && s[i - len] == s[i + len]) ++len;
      --len;
      if (2 * len + 1 > maxLength) {
	maxLength = 2 * len + 1;
	re_i = i - len;
      }

      len = 0;
      while (i - len >= 0 && i + len + 1 < s.length() && s[i - len] == s[i + len + 1]) ++len;
      --len;
      if (2 * len + 2 > maxLength) {
	maxLength = 2 * len + 2;
	re_i = i - len;
      }
    }
    return s.substr(re_i, maxLength);
  }
};
