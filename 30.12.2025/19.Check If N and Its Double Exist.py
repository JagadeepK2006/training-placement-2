class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        doublemap={}
        halfmap={}
        zerocounter=0
        for index,value in enumerate(arr):
            if value!=0:
                double = value*2
                if value%2==0:
                    half = value/2
                    if half not in halfmap:
                        halfmap[half]=value
                if double not in doublemap:
                    doublemap[double]=value
            elif value==0:
                zerocounter +=1
            if (value!=0 and (value in doublemap or value in halfmap)) or zerocounter>1:
                    return True
        return False   
