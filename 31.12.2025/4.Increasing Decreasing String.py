class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic={}
        string=''
        for i in s:
            dic[i]=dic.get(i,0) +1
        while dic:
            for cc in sorted(dic.keys()):
                string += cc
                dic[cc] -= 1
                if dic[cc] == 0:
                    del dic[cc]
            if not dic:
                break

            for cc in sorted(dic.keys(), reverse=True):
                string += cc
                dic[cc] -= 1
                if dic[cc] == 0:
                    del dic[cc]

        return string
