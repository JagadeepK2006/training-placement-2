from datetime import date
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        parts1=date1.split('-')
        year1=int(parts1[0])
        month1=int(parts1[1])
        dt1=int(parts1[2])

        parts2=date2.split('-')
        year2=int(parts2[0])
        month2=int(parts2[1])
        dt2=int(parts2[2])

        days_count=abs(date(year2,month2,dt2)-date(year1,month1,dt1))

        return days_count.days
        
