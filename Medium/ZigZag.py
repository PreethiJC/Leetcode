class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        listStr = []
        for i in range(numRows):
            listStr.append("")
        idx = 0
        sign = -1
        j = 0
        if numRows == 1:
            return s
        for st in s:
            j += 1
            index = (idx - j * sign)
            listStr[index - 1] += st

            if index == numRows:
                idx = numRows
                sign = 1
                j = 0
            elif index == 1:
                idx = 0
                sign = -1
                j = 1
        return ''.join(listStr)



soln = Solution()
print(soln.convert("PAYPALISHIRING", 3))