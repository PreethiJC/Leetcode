class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxArea = 0
        while(i < j):
            area = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return maxArea

s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
