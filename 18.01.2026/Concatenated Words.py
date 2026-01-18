class Solution:
    def findAllConcatenatedWordsInADict(self, w):
        s=set(w); r=[]
        def dfs(x):
            for i in range(1,len(x)):
                if x[:i] in s and (x[i:] in s or dfs(x[i:])):
                    return True
            return False
        for x in w:
            s.remove(x)
            if dfs(x): r.append(x)
            s.add(x)
        return r
