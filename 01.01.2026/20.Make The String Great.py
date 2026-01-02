class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        mapping = {}

        for l, u in zip(ascii_lowercase, ascii_uppercase):
            mapping[l] = u
            mapping[u] = l
        
        for char in s:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
        
        
