class Solution(object):
    def minSubsequence(self, nums):
        answer = []
        nums.sort(reverse = True)
        sum1 = 0
        sum2 = sum(nums)
        for number in nums:
            sum1 += number
            sum2 -= number
            answer.append(number)
            if sum1 > sum2:
                return answer 
