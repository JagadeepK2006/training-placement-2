class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n%2 == 0:
            return 'g'*(n-1) + 'h'
        else:
            return 'g'*n
