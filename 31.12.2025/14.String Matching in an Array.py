class Solution(object):
    def stringMatching(self, words):
        w=[]
        for i in range(len(words)):
            for j in words:
                if(words[i] in j and words[i]!=j):
                    w.append(words[i])
        return list(set(w))
        
