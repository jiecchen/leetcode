class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        sol = set([])
        num = sorted(num)
        count = {} # count the frequencies
        for x in num:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        #
        for i in xrange(0, len(num)):
            for j in xrange(i + 1, len(num)):
                c = -num[i] - num[j]
                if c >= num[j]:
                   if count.setdefault(c, 0) >= [num[i], num[j], c].count(c):
                       sol.add((num[i], num[j], c))
                else:
                    break
        return [list(x) for x in sol]

S = [-1, 0, 1, 1, 1,  2, -1, -4, 10, -5, -6]
s = Solution()
print s.threeSum(S)
