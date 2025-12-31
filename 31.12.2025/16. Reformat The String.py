class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        lets = []
        nums = []
        ll = 0
        ln = 0
        for i in s:
            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
                ln += 1
                nums.append(i)
            else:
                ll += 1
                lets.append(i)
        print lets
        print nums
       
        if abs(ln - ll) > 1:
            return ""
        ret = ""
        index = 0
        if ll == ln:
            while index < ll:
                ret += lets.pop(0)
                ret += nums.pop(0)
                index += 1
        elif ll < ln:
            ret += nums.pop(0)
            while index < ll:
                ret += lets.pop(0)
                ret += nums.pop(0)
                index += 1
        elif ln < ll:
            ret += lets.pop(0)
            while index < ln:
                ret += nums.pop(0)
                ret += lets.pop(0)
                index += 1
        print lets
        print nums
        print ret
        return ret
        
        
