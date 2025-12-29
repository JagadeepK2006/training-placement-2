class Solution(object):
    def dayOfYear(self, date):
        def artikyil(n):
            if n%4==0:
                if n%100==0 and n%400!=0:
                    return False
                else:
                    return True
        yilgun=0
        a=date.split("-")
        yilgun=yilgun+int(a[2])
        ay=1
        if artikyil(int(a[0])) and int(a[1])>2:
            yilgun=yilgun+1
        while int(a[1])>ay:
            if ay==2:
                yilgun=yilgun+28
            elif ay<=7:
                if ay%2==1:
                    yilgun=yilgun+31
                else:
                    yilgun=yilgun+30
            else:
                if ay%2==0:
                    yilgun=yilgun+31
                else:
                    yilgun=yilgun+30
            ay=ay+1
        return yilgun
        
