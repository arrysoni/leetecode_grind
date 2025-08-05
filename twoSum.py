class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # This is a hashmap based solution

        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                print("[dic[target - num], i]:", [dic[target - num], i])
                return [dic[target - num], i]
            dic[num] = i


nums1 = [3, 2, 4]
Solution().twoSum(nums1, 6)

nums2 = [2, 7, 11, 15]
Solution().twoSum(nums2, 9)

nums3 = [3, 3]
Solution().twoSum(nums3, 6)
