class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start_cities = set()
        dest_cities = set()        
        for start, dest in paths:
            start_cities.add(start)
            dest_cities.add(dest)
        for city in dest_cities:
            if city not in start_cities:
                return city
        return ""
