class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}   
        pairs = 0   
        for num in nums:
            freq[num] = freq.get(num, 0) + 1  
        for k in freq.keys():
            if freq[k] > 1:
                pairs += freq[k] * (freq[k] - 1) // 2 
        return pairs
