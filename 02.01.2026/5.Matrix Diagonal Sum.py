class Solution(object):
    def diagonalSum(self, mat):
        i = 0
        k = len(mat[0])
        j = k -1
        s1 = 0
        while(i < k and j >= 0):
            s1 += mat[i][i] + mat[i][j]
            i += 1
            j -= 1

        if k % 2 == 1:
            s1 -= mat[k//2][k//2]
        return s1


        
