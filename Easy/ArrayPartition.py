class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = 0
        if len(nums) <= 2:
            return sum(nums)
        while nums:
            a += min(nums.pop(), nums.pop())
        return a

s = Solution()
print s.arrayPairSum([1, 4, 3, 2])