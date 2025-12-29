class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = []
        ss.append(s[0])
        for i in range(1,len(s)):
             if len(ss) != 0 and ss[-1] == s[i]:
                ss.pop()
             else :
                ss.append(s[i])
        
        return ''.join(ss)

        
