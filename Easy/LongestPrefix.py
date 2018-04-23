import sys
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        strs.sort()
        prefix = ""
        minWrd = min(strs, key=len)
        low = 0
        high = len(minWrd) - 1
        while low <= high:
            middle = (low + high) / 2
            flag = True
            for word in strs:
                if not word.startswith(minWrd[:middle + 1]):
                    flag = False

            if flag:
                low = middle + 1
                prefix = minWrd[:middle + 1]
            else:
                high = middle - 1

        return prefix

S = Solution()
print(S.longestCommonPrefix(["c","c"]))









