class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        print(nums)


nums1 = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums1)

nums2 = [0]
Solution().moveZeroes(nums2)
