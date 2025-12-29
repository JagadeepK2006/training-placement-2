class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        import datetime
        d=datetime.date(year,month,day)
        days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        return days[d.weekday()]

        
