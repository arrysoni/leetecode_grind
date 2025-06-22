"""
169. Majority Element
Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3, 2, 3]
Output: 3

Example 2:
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        print('The majority element is: ', candidate)

        return candidate


nums1 = [3, 2, 3]
Solution().majorityElement(nums1)

nums2 = [2, 2, 1, 1, 1, 2, 2]
Solution().majorityElement(nums2)
