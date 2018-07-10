class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            val = nums.pop()
            nums.insert(0, val)
            k -= 1

nums = [1,2,3,4,5,6,7]
s = Solution()
s.rotate(nums, 3)
print nums
