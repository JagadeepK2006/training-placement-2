class Solution(object):
    def freqAlphabets(self, s):
        word = []
        i =0
        a_dict = {idx:c for idx, c in enumerate(string.ascii_lowercase, start=1)}
        while i < len(s):
            if i +2 < len(s) and s[i+2] == '#':
                word.append(a_dict[int(s[i]+s[i+1])])
                i += 3
            else: 
                word.append(a_dict[int(s[i])])
                i +=1
        return ''.join(word)

                

        
