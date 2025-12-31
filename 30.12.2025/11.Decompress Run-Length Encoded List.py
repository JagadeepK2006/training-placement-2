class Solution(object):
    def decompressRLElist(self, nums):
        new_list =[]
        for i in range(len(nums)):
            if i % 2 == 0: 
                s,v = nums[i],nums[i+1]
                for j in range(s):
                    new_list.append(v)
        return new_list

            
        
