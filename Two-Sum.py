class Solution:
    def __init__(self):
        self.M = 100000
        self.h = [0] * self.M

    def twoSum(self, num, target):
        pos = [0] * self.M
        for i in range(len(num)):
            self.h[num[i]] = self.h[num[i]] + 1
            pos[num[i]] = i 
        # special case:
        if target % 2 == 0 and self.h[target / 2] > 1:
            ans = []
            for i in range(len(num)):
                if num[i] + num[i] == target:
                    ans.append(i + 1)
            return tuple(ans)
        for x in num:
            if x > target:
                continue
            if self.h[x] > 0  and  self.h[target - x] > 0:
                if x * 2 == target and self.h[x] < 2:
                    continue
                else:
                    return (pos[x] + 1, pos[target - x] + 1)


