import bisect

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        l = bisect.bisect_left(A, target)
        r = bisect.bisect_right(A, target)
        if l >= len(A) or A[l] != target:
            l = -1
        if r <= 0 or A[r - 1] != target:
            r = 0
        return [l, r - 1]


A = [5, 7, 7, 8, 8, 10]
sol = Solution()
print sol.searchRange(A, 8)
