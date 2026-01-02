class Solution(object):
    def maxDepth(self, s):
        count = 0
        ans = 0
        for ch in s :
            if ch == '(' :
                count += 1
                ans = max(ans , count)
            elif ch == ')' :
                count -= 1
                ans = max(ans , count)
            else :
                continue
        return ans
        
        
