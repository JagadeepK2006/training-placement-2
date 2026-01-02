class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        nums.sort()

        unique_nums = []

        for num in nums:
            if num not in unique_nums:
               unique_nums.append(num)

        freq_list = []
        for num in unique_nums:
            freq = nums.count(num)
            freq_list.append([num, freq])

        freq_list.sort(key=lambda x: (x[1], -x[0]))

        for pair in freq_list:
            number = pair[0]
            frequency = pair[1]
            for _ in range(frequency):
                result.append(number)

        return result
