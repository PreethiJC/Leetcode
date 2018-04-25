class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        sarr = " ".join(s.split()).split(" ")
        return " ".join(sarr[::-1])