class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        n = len(nums)
        if n == 0 or n == 1:
            return n
        for i, n in enumerate(nums):
            if i < len(nums) - 1:
                if nums[i] != nums[i + 1]:
                    nums[j] = nums[i]
                    j += 1
            else:
                break
        nums[j] = nums[i]
        return j+1

s = Solution()
s.removeDuplicates([1, 1, 2])