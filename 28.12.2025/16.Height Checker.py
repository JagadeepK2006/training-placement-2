class Solution(object):
    def heightChecker(self, heights):
        c = 0
        s = sorted(heights)
        for i in range(len(heights)):
            if s[i] != heights[i]:
                c += 1
            else: pass
        return c 
        
