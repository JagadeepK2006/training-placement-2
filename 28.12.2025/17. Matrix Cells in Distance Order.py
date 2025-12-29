class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        cell = [[r,c] for r in range(rows) for c in range(cols)]
        cell.sort(key= lambda x:abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return cell
        
