class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        # Start with any valid triplet sum (first three after sort)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Optional: skip duplicate anchors (not required for correctness)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                # Update best if this sum is closer to target
                if abs(s - target) < abs(closest - target):
                    closest = s

                # Move pointers to get closer to the target
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    # Exact hit — can't get closer than this
                    return target

        return closest


# Test cases
solution = Solution()

nums1 = [-1, 2, 1, -4]
target1 = 1
print(solution.threeSumClosest(nums1, target1))  # Expected: 2

nums2 = [0, 0, 0]
target2 = 1
print(solution.threeSumClosest(nums2, target2))  # Expected: 0

# You can add more
nums3 = [1, 1, 1, 0]
target3 = -100
print(solution.threeSumClosest(nums3, target3))  # Expected: 2 (1+1+0)
