class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in numDict:
                return [numDict[complement], i]
            numDict[n] = i

s = Solution()
print s.twoSum([5,2,5], 10)




