class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A) < 1:
            return 0
        l = 0
        r = len(A) - 1
        while l <= r:
            while r > l and A[l] != elem:
                l += 1
            while r > l and A[r] == elem:
                r -= 1
            if r > l:
                A[r], A[l] = A[l], A[r]
                l += 1
                r -= 1
            if r <= l:
                if elem == A[r]:
                    return r
                else:
                    return r + 1



A = [1, 1]
s = Solution()
print s.removeElement([4, 5], 4) 
        
