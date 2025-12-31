class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def adjuster(number_1, number_2):
            """gets two numbers and removes all zeroes from them"""
            if '0' in str(number_1) or '0' in str(number_2):
                return adjuster(number_1 + 1, number_2 - 1)
            return [number_1, number_2]
        
        mid_num_1 = 1
        mid_num_2 = n - 1
        return adjuster(mid_num_1, mid_num_2)
