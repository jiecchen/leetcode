class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) < 1:
            return ""
        l = 0
        while True:
            if len(strs [0]) <= l:
                return strs[0][0:l]
            ch = strs[0][l]
            for s in strs:
                if (len(s) <= l) or s[l] != ch:
                    return s[0:l]
            l = l + 1
            


s = Solution()
strs = [""]
print s.longestCommonPrefix(strs)
