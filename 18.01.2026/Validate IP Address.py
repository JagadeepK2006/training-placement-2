class Solution:
    def validIPAddress(self, q):
        if q.count('.')==3:
            p=q.split('.')
            for x in p:
                if not x.isdigit() or (x[0]=='0' and len(x)>1) or not 0<=int(x)<=255:
                    return "Neither"
            return "IPv4"
        if q.count(':')==7:
            p=q.split(':')
            h="0123456789abcdefABCDEF"
            for x in p:
                if not 1<=len(x)<=4 or any(c not in h for c in x):
                    return "Neither"
            return "IPv6"
        return "Neither"
