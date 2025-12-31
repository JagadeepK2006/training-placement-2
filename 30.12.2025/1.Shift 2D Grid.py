class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        flat = []
        for i in grid:
            for j in i:
                flat += [j]
        for n in range(k):
            temp = flat[-1]
            temp2 = flat[:-1]
            flat = []
            flat.append(temp)
            for x in temp2:
                flat.append(x)
        rows = len(grid)
        cols = len(grid[0])
        ret = []
        index = 0
        for a in range(rows):
            temp = []
            for b in range(cols):
                temp.append(flat[index])
                index += 1
            ret.append(temp)
        return ret
