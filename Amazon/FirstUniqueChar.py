from collections import OrderedDict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        sDict = OrderedDict()
        for a in s:
            if a in sDict:
                sDict[a] += 1
            else:
                sDict[a] = 0

        for a in sDict:
            if sDict[a] == 0:
                print a
                return s.index(a)
        return -1

s = Solution()
print s.firstUniqChar("loveleetcode")

