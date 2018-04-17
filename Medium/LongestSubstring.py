class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        j = 0
        i = 0
        ans = 0
        strDict = dict()
        while j < n:
            i = max(strDict.get(s[j]), i)
            ans = max(ans, j-i+1)
            strDict[s[j]] = j+1
            j += 1
        return ans

s = Solution()
print(s.lengthOfLongestSubstring("bacade"))
