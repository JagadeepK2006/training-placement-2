class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        new_ls=[]
        for i in range(0,len(nums)):
            new_ls.insert(index[i],nums[i])
        return new_ls
