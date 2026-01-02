class Solution(object):
    def reformatDate(self, date):
        from datetime import datetime
        parts = date.split()
        day = parts[0][:-2] 
        month = parts[1]
        year = parts[2]
        date_str = "%s %s %s" % (day, month, year)
        dt = datetime.strptime(date_str, "%d %b %Y")
        return dt.strftime("%Y-%m-%d")
