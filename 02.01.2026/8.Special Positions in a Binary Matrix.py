class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        r = len(mat)
        c = len(mat[0])
        special_count = 0
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    row_sum = sum(mat[i][k] for k in range(c))
                    col_sum = sum(mat[k][j] for k in range(r))
                    
                    if row_sum == 1 and col_sum == 1:
                        special_count += 1
                        
        return special_count

                    
      
                    

        
