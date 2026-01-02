class Solution(object):
    def finalPrices(self, prices):
        stack = []
        
        for i, current in enumerate(prices):
           
            while stack and prices[stack[-1]] >= current:
                waiting_index = stack.pop()
                prices[waiting_index] -= current
            
            stack.append(i)
            
        return prices
