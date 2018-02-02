class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        sign = 1
        if x < 0:
            sign = -1
            x *= sign

        place = pow(10, len(str(x)) - 1)
        while x != 0:
            y += (x%10 * place)
            place /= 10
            print y, x
            x /= 10
        if self.isInt32(y):
            return 0
        return y*sign

    def isInt32(self, x):
        return not(len(bin(x)[2:]) < 32)

s = Solution()
print(s.reverse(1563847412))