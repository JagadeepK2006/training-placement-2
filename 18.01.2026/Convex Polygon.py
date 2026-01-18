class Solution:
    def isConvex(self, p):
        s=0
        for i in range(len(p)):
            x1,y1=p[i]
            x2,y2=p[(i+1)%len(p)]
            x3,y3=p[(i+2)%len(p)]
            c=(x2-x1)*(y3-y2)-(y2-y1)*(x3-x2)
            if c:
                if s and c*s<0: return False
                s=c
        return True
