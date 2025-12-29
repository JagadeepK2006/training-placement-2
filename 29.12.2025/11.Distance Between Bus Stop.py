class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        left_distance = 0

        i = start

        while i != destination:
            left_distance += distance[i]

            i = (i + 1) % len(distance)
        
        i = start

        print(left_distance)

        right_distance = 0

        while i != destination:

            i -= 1

            if i < 0:
                i = len(distance) - 1

            right_distance += distance[i]
        
        print(right_distance)

        return min(left_distance, right_distance)
