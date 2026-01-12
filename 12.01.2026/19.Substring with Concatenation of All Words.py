class Solution(object):
    
    def findSubstring(self, s, words):
        n, m, r = len(words), len(words[0]) if words else 0, []
        counter = collections.Counter(words)

        for i in xrange(m):
            localCout = collections.defaultdict(int)
            window = collections.deque()

            for j in xrange(i, len(s), m):
                word = s[j:j + m]
                if word in counter:
                    localCout[word] += 1
                    window.append(word)

                    while localCout[word] > counter[word]:
                        localCout[window.popleft()] -= 1

                    if len(window) == n:
                        r.append(j - (n - 1) * m)
                else:
                    localCout.clear()
                    window.clear()
        return r
