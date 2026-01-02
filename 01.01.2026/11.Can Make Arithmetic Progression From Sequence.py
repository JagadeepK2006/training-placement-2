class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) == 2:
            return True
        else:
            sorted_list = sorted(arr)
            diff = sorted_list[1] - sorted_list[0]
            for i in range(1, len(sorted_list)):
                if sorted_list[i] - sorted_list[i - 1] != diff:
                    return False
            return True
        
