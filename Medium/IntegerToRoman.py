from bisect import bisect_left
from collections import OrderedDict
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # adding subtractive cases as well.
        vals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

        res = ""

        for val in vals[::-1]:
            if num >= val:
                q = num / val
                num = num % val
                res += symbols[vals.index(val)] * q

        return res

s = Solution()
print(s.intToRoman(1994))












