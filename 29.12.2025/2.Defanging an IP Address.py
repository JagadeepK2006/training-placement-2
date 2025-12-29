class Solution(object):
    def defangIPaddr(self, address):
        k = ""
        for i in address:
            if i == '.':
                k += "[.]"
            else:
                k += i
        return k
