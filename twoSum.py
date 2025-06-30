class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if ((len(nums) == 1) and (nums[0] == target)):
            return [nums[0]]

        for left in range(len(nums)):
            for right in range(left+1, len(nums)):
                if ((nums[left]+nums[right]) == target):
                    print(f"[{left},{right}]")
                    return [left, right]


nums1 = [3, 2, 4]
Solution().twoSum(nums1, 6)

nums2 = [2, 7, 11, 15]
Solution().twoSum(nums2, 9)

nums3 = [3, 3]
Solution().twoSum(nums3, 6)
