class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        start = rounds[0]
        end = rounds[-1]
        visited = []
        while end != start:
            visited.append(end)
            end -=1
            if end == 0:
                end = n

        visited.append(start)
        visited.sort()
        return visited



        
