class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)  # length of the string
        i = n - 2   # we need a safe space for i+1 and i to be compared

        # we start checking from the right side [1,3,2], making our pivot go to '1' here
        while i >= 0 and nums[i] > nums[i+1]:
            i -= 1

        # in case no pivot is found, we will have to reverse the whole array, say we have [3,2,1]
        if i >= 0:

            # find the rightmost successor
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # swap
            nums[i], nums[j] = nums[j], nums[i]

        # clean up the right side, everything after the swap must be as small as possible, so we reverse the right side
        # because smaller right side = smallest possible next number
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums


nums1 = [1, 2, 3]
print(Solution().nextPermutation(nums1))

nums2 = [3, 2, 1]
print(Solution().nextPermutation(nums2))

nums3 = [1, 1, 5]
print(Solution().nextPermutation(nums3))
