class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) >= 2:
            y = stones.pop(stones.index(max(stones)))
            x = stones.pop(stones.index(max(stones)))
            
            if x != y:
                stones.append(y - x)

        if stones:
            return stones[0]
        else:
            return 0
