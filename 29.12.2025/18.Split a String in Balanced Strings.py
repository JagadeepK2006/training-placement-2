class Solution(object):
    def balancedStringSplit(self, s):
        ans = 0
        count = 0
        for i in s:
            if i == "L":
                count += 1
            elif i == "R":
                count -= 1
            if count == 0:
                ans += 1
        return ans
        
