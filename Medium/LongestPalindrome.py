class Solution(object):
    def longestPalindrome(self, word):
        sub = word[::-1]
        subStr = self.longestSubstring(word, sub)
        if subStr == subStr[::-1]:
            return subStr
        else:
            return word[0]

    def longestSubstring(self, word, sub):
        li = [[0] * (len(word) + 1) for i in range((len(word) + 1))]
        li = self.getMatrix(li, word, sub)
        j, subLen = self.getLenLongestSubstring(li)
        return self.getLongestSubstring(subLen, j, sub)

    def getMatrix(self, li, word, sub):
        i = 1
        for w in word:
            j = 1
            for s in sub:
                if w == s:
                    li[i][j] = (li[i - 1][j - 1]) + 1
                else:
                    li[i][j] = 0
                j += 1
            i += 1
        return li

    def getLenLongestSubstring(self, li):
        subLen = 0
        i = 1
        for lis in li[1:]:
            maxVal = max(lis)
            if subLen <= maxVal:
                subLen = maxVal
                j = lis.index(maxVal)
            i += 1
        return j, subLen

    def getLongestSubstring(self, subLen, j, sub):
        substr = sub[j - 1]
        i = 0
        while i < subLen - 1:
            j -= 1
            substr += sub[j - 1]
            i += 1
        return substr