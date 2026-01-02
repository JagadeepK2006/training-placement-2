class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        for i, word in enumerate(words, 1):
            if word.startswith(searchWord):
                return i
        return -1
