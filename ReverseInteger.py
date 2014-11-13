class Solution:
    # @return an integer
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1
        s = str(abs(x))
        s = s[::-1]
        num = int(s)
        # if num exceed the maximum integer, output zero
        # stupid data
        if num >= 2147483647:
            num = 0
        return sign * num


