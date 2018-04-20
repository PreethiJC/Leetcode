class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numDict = {}
        for n in nums:
            if n in numDict:
                numDict.pop(n)
            else:
                numDict[n] = 1

        return numDict.keys()[0]
