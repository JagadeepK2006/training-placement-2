class Solution(object):
    def findSpecialInteger(self, arr):
        li=[]
        a=arr
        b=set(a)
        c=list(b)
        for i in c:
            li.append(arr.count(i))
        z=max(li)
        return c[li.index(z)]
        
