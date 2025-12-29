class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        dic={}

        for i in range(0,len(arr)):
            if arr[i] not in dic.keys():
                dic[arr[i]]=0
            
            dic[arr[i]]+=1
        
        return len(set(dic.values()))==len(dic.values())
        
