class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        l=[]
        x=0
        y=0
        for ch in path:
            l.append([x,y])
            if (ch=='N'):
                y+=1
            elif (ch=='S'):
                y-=1
            elif (ch=='E'):
                x+=1
            else:
                x-=1
            if [x,y] in l:
                return True
        return False
