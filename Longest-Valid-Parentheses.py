class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        ans = 0
        ct = 0
        sk = []
        for a in s:
            if a == ')': # need pop
                if len(sk) == 0:
                    ct = 0
                else:
                    ct += 1
                    sk.pop()
                    if (len(sk) > 0):
                        ans = max([ ans, ct - sk[-1] ])
                    else:
                        ans = max([ ans, ct ])
            else: # need push
                ct += 1
                sk.append(ct)
        return ans

sol = Solution()
print sol.longestValidParentheses("))()())))")
