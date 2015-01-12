class Solution:
    # @return a boolean
    def isValid(self, s):
        stk = []
        pairs = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in ('(', '{', '['):
                stk.append(c)
            else:
                if len(stk) <= 0 or stk.pop() != pairs[c]:
                    return False
        return stk == []


s = Solution()
print s.isValid('{[()(([(]])]))]}')
