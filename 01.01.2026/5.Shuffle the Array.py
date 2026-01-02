class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l1=nums[:n]
        l2=nums[n:]
        print(l1,l2)
        ans=[]
        for i in range(n):
            ans.append(l1[i])
            ans.append(l2[i])
        return ans

        
