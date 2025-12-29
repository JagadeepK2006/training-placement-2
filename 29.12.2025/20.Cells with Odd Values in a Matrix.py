class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix=[]
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(0)
            matrix.append(row)
        for e in indices:
            row=e[0]
            col=e[1]
            for i in range(m):
                matrix[i][col]+=1
            for j in range(n):
                matrix[row][j]+=1
        count=0
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]%2!=0):
                    count+=1
        return count
