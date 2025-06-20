"""
Problem Description:

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place
such that each unique element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in `nums`.

The number of unique elements should be stored as `k`.

To get accepted, your solution must:
1. Modify the input array `nums` such that the first `k` elements contain the unique elements
   in the same order as they appeared.
2. Return `k`.
3. The values beyond index `k-1` in `nums` do not matter.

The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

If all assertions pass, then your solution will be accepted.

Examples:

Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Initialize the slow pointer
        k = 1

        # Iterate through the list starting from index 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


nums1 = [1, 1, 2]
Solution().removeDuplicates(nums1)

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Solution().removeDuplicates(nums2)
