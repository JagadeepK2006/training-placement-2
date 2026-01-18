class Solution:
    def islandPerimeter(self, g):
        r=0
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]:
                    r+=4
                    if i and g[i-1][j]: r-=2
                    if j and g[i][j-1]: r-=2
        return r
