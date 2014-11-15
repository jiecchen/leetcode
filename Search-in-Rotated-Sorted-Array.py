import bisect

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integerA

    def bsearch(self, A, target):
        idx = bisect.bisect_left(A, target)
        if 0 <= idx < len(A) and A[idx] == target:
            return idx
        else:
            return -1
            
    def mplus(self, a, b):
        if a < 0  or b < 0:
            return -1
        return a + b

    def search(self, A, target):
        if len(A) == 0:
            return -1
        if len(A) < 10:
            for i in xrange(len(A)):
                if A[i] == target:
                    return i
            return -1

        mid = len(A) / 2
        if A[mid] == target:
            return mid

        # assume not rotated
        tmp = self.bsearch(A, target)
        if tmp >= 0 and tmp < len(A) and A[tmp] == target:
            return tmp
    
        # print "mid =", mid, "A =", A
        if A[mid] > A[0]:
            if target >= A[mid]:
                return self.mplus(mid + 1, self.search(A[mid + 1 :], target))
            else: # target < A[mid]
                if target <= A[-1]:
                    return self.mplus(mid + 1, self.search(A[mid + 1 :], target))
                else: # target > A[-]
                    return self.bsearch(A[: mid], target)

        else: # A[mid] < A[0]
            if target <= A[mid]:
                return self.search(A[: mid + 1], target)
            else:
                if target > A[-1]:
                    return self.search(A[: mid], target)
                else:
                    return self.mplus(mid + 1, self.bsearch(A[mid + 1:], target))




