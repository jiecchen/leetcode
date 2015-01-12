class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num) - 1
        while n > 0:
            if num[n - 1] >= num[n]:
                n -= 1
            else: # num[n - 1] < num[n]
                m = len(num) - 1
                while num[m] <= num[n - 1]:
                    m -= 1
                num[m], num[n - 1] = num[n - 1], num[m]
                l = n
                r = len(num) - 1
                while l < r:
                    num[l], num[r] = num[r], num[l]
                    l += 1
                    r -= 1
                return num
        return sorted(num)

A = [1, 1, 5]

sol = Solution()
print sol.nextPermutation(A)
        



