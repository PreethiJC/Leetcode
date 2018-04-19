class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr = list()
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

        if i == len(nums1):
            arr.extend(nums2[j:])
        else:
            arr.extend(nums1[i:])

        b = len(arr) / 2
        if len(arr) % 2 == 0:
            a = (len(arr)/2) - 1
            median = (arr[a] + arr[b])/2.0
        else:
            median = arr[b]

        return median
