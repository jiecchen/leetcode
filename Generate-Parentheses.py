class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0:
            return [""]
        ans = []
        for i in range(n):
            ans1 = self.generateParenthesis(i) 
            ans2 = self.generateParenthesis(n - i - 1)
            for x in ans1:
                for y in ans2:
                    ans.append("(" + x + ")" + y)
        return ans


s = Solution()
print s.generateParenthesis(3)
