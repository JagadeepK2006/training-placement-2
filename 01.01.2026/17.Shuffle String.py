class Solution(object):
    def restoreString(self, s, indices):
        a = [''] * len(s) 
        for i in range(len(s)):
            a[indices[i]] = s[i] 
        return ''.join(a)
