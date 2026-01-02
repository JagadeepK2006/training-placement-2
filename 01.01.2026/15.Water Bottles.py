class Solution(object):
    def __init__(self):
        self.remainder=0

    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        self.remainder+=((numBottles)%numExchange) 
        if self.remainder%numExchange == numExchange - 1 and numBottles < numExchange and self.remainder > numExchange:
            self.remainder = self.remainder + 1

        if numBottles<numExchange :
            return (numBottles%numExchange)+((self.remainder)//numExchange)
        else:
            return numBottles + self.numWaterBottles(numBottles//numExchange,numExchange)
        
