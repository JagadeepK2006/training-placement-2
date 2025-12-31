class Solution(object):
    def kWeakestRows(self, mat, k):
        l=[]
        for i,value_row in enumerate(mat):
            soldier_c=sum(value_row)
            l.append([i,soldier_c])            
        sort=sorted(l,key= lambda x: (x[1], x[0]))
        return [sort[i][0] for i in range (0,k)]





        
