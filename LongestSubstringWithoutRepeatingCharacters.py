# run in linear time in terms of the size of the string

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        n = 0
        currentLength = 0
        maxLength = 0
        dc = {}
        for a in s:
            n += 1

            if not dc.has_key(a):
                dc[a] = n - 1
                currentLength += 1
                if currentLength > maxLength:
                    maxLength = currentLength

            else: # some repeat chars
                start = n - currentLength - 1

                # update the length
                currentLength = n - dc[a] - 1

                # remove all useless keys
                for i in range(start, dc[a] + 1):                    
                    del dc[s[i]]

                # update key
                dc[a] = n - 1

        return maxLength



