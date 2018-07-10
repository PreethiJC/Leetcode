class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for l in t:
            if l in s:
                s = s.replace(l, '', 1)
            else:
                return False
        if s == '':
            return True
        else:
            return False

s = Solution()
print s.isAnagram("anagram", "nagaram")
print s.isAnagram("a", "ab")