"""
Leetcode 283. Move Zeroes
Difficulty: Easy

Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note:
- You must do this in-place without making a copy of the array.

Examples:
Input:  nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input:  nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1
"""


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
