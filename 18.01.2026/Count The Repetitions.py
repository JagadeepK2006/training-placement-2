class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        i=j=cnt=0
        d={}
        while i<n1:
            for c in s1:
                if c==s2[j]:
                    j+=1
                    if j==len(s2):
                        j=0; cnt+=1
            i+=1
            if j in d:
                pi,pc=d[j]
                loop=i-pi
                inc=cnt-pc
                k=(n1-i)//loop
                cnt+=k*inc
                i+=k*loop
            else:
                d[j]=(i,cnt)
        return cnt//n2
