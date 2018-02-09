class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sUpper = s.upper()
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dig = 0
        for i, v in enumerate(s):
            if i != len(s) - 1:
                if symbols[v] < symbols[sUpper[i+1]]:
                    dig -= symbols[v]
                else:
                    dig += symbols[v]
            else:
                dig += symbols[v]
        return dig

s = Solution()
print(s.romanToInt("MCMLXXXIV"))


