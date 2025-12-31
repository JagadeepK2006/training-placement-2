class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)

        for i in range(1,n):
            nums[i]+=nums[i-1]
        
        val=min(nums)
        if val<1:
            return abs(min(nums))+1
        else:
            return 1
