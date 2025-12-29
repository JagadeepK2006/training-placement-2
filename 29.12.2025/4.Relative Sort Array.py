class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        freq = Counter(arr1)
        result = []

        for num in arr2:
            result.extend([num]*freq[num])
            del freq[num]

        for num in sorted(freq):
            result.extend([num]*freq[num])
        return result
