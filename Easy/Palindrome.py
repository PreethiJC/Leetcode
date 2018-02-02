class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = 0
        orig = x
        sign = 1
        if x < 0:
            return False
            # sign = -1
            # x *= sign

        place = pow(10, len(str(x)) - 1)
        while x != 0:
            y += (x % 10 * place)
            place /= 10
            x /= 10

        return y * sign == orig

s = Solution()
print(s.isPalindrome(-2147447412))