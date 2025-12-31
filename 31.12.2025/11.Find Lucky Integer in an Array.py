class Solution(object):
    def findLucky(self, arr):
        return max([num for num in arr  if arr.count(num) == num] or[-1])
