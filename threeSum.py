class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)

        for i, x in enumerate(nums):
            if i > 0 and x == nums[i - 1]:
                continue          # skip duplicate anchors
            if x > 0:
                break             # no triplet can sum to 0 beyond this

            l, r = i + 1, n - 1
            target = -x
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([x, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates on both sides
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res
