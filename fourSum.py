class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []

        if n < 4:
            return res

        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]:
                continue

            # pruning for i
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # pruning for j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res


# Test cases
sol = Solution()

nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
print(sol.fourSum(nums1, target1))
# Expected: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

nums2 = [2, 2, 2, 2, 2]
target2 = 8
print(sol.fourSum(nums2, target2))
# Expected: [[2, 2, 2, 2]]

nums3 = [0, 0, 0, 0]
target3 = 0
print(sol.fourSum(nums3, target3))
# Expected: [[0,0,0,0]]
