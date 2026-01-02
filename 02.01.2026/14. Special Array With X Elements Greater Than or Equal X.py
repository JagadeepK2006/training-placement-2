class Solution(object):
    def specialArray(self, nums):
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2
            count = sum(1 for num in nums if num >= mid)

            if count == mid:
                return mid
            elif count > mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1
