class Solution(object):
    def minOperations(self, logs):
        main=0
        for x in logs:
            if x.count(".")==0:
                main=main+1
            elif x.count(".")==2 and main>0:
                main=main-1
        return main
        
