class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        Dict={"even":0,"odd":0}
        for x in position:
            if x%2==0:
                Dict["even"]+=1
            else:
                Dict["odd"]+=1
        if Dict["even"]==0 or Dict["odd"]==0:
            return 0
        else:
            return min(Dict["even"],Dict["odd"])
        
