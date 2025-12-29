class Solution(object):
    def countCharacters(self, words, chars):
        supply = Counter(chars)
        total = 0
        for word in words:
            need = Counter(word)
            if all(need[c] <= supply[c] for c in need):
                total += len(word)
        return total
