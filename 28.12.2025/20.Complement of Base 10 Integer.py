class Solution(object):
    def bitwiseComplement(self, num):
        """
        :type n: int
        :rtype: int
        """
        if num == 0: return 1
        mask = 0
        temp = num
        while temp:
             mask = (mask<<1)|1
             temp >>= 1
        return num ^ mask
