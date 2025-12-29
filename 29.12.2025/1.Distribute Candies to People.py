class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans=[0]*num_people
        give=1
        i=0
        
        while candies>0:
            give_to=min(give,candies)
            ans[i%num_people]+=give_to
            candies-=give
            give+=1
            i+=1
        return ans
