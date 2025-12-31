class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp = 0
        flag = False
        n = len(nums)
        for i in range(n):
            if nums[i]==0:
                temp+=1
            else:
                if flag and temp<k:
                    return False
                if not flag:
                    flag = True
                temp=0
        return True
