class Solution(object):
    def findOcurrences(self, text, first, second):
        res = []
        b = text.split()
        n = len(b)
        for i in range(n-2):
            if b[i] == first and b[i+1] == second:
                res.append(b[i+2])
        return res
        
