class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, n in enumerate(nums):
            if n != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j+=1
        print nums

s = Solution()
s.moveZeroes([3,0,0,1])