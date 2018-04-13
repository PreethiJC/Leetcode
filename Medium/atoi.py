class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = 0
        place = 1
        str = str.strip()
        if len(str) == 0:
            return num
        numDict = {'1': 1, '2': 2, '3': 3, '4': 4,
                   '5': 5, '6': 6, '7': 7, '8': 8,
                   '9': 9, '0': 0}


        for s in str[::-1][:len(str)-1]:
            if s in numDict:
                nnum = place * numDict[s]
                num += nnum
                place *= 10
            else:
                num = 0

        if str[0] == '-':
            num *= -1
        elif str[0].isdigit():
            num = numDict[str[0]]
        elif str[0] != '+':
            num = 0

        if num >= 2147483647:
            return 2147483647
        if num <= -2147483647:
            return -2147483647

        return num

s = Solution()
print(s.myAtoi("+1"))


