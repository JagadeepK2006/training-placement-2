class Solution(object):
    def luckyNumbers(self, matrix):
        min_in_rows = [min(row) for row in matrix]
        max_in_cols = [max(col) for col in zip(*matrix)]
        return list(set(min_in_rows) & set(max_in_cols))
        
