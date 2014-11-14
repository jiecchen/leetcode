class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        wl = len(L[0])
        wc = len(L)
        idx = []
        # build dict for L
        dl = {}
        for w in L:
            dl[w] = dl.setdefault(w, 0) + 1

        
        # start from 0
        for st in range(wl):
            s = S[st:]
            ct = 0 # how many words match so far
            i = 0
            ds = {}
            while (i * wl + wl <= len(s)):
                w = s[(i * wl) : (i * wl + wl)] # current word 
                hw = s[(i - ct) * wl : (i - ct + 1) * wl] # head word!!
                if dl.setdefault(w, 0) == 0:  # no such word
                    ct = 0
                    ds = {}
                elif ds.setdefault(w, 0) + 1 > dl[w]: # overflow :-)
                    if hw <> w: # fails
                        ct = 0
                        ds = {}
                        # else, do nothing, drop the dead, and use current
                else: # successful matching!
                    ct += 1
                    ds[w] = ds.setdefault(w, 0) + 1
                    if ct == wc: # now we have full matching
                        idx.append((i - wc + 1) * wl + st)
                        # drop the head
                        ct -= 1
                        ds[hw] -= 1 
                i += 1
        return idx
                
                
            
            
sol = Solution()
print sol.findSubstring("cabcdabab cd",["ab","cd", "ab"])
