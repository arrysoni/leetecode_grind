class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # Delete val in the list
        for ele in nums[:]:
            print(ele)
            if ele == val:
                nums.remove(ele)

        print(nums)
        return len(nums)


# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2


# print(Solution().removeElement(nums, val))

def custom_judge(removeElement_fn, nums, val, expectedNums):
    # Make a working copy because the function modifies nums in-place
    arr = nums[:]  

    k = removeElement_fn(arr, val)

    # Assert k matches expected length
    assert k == len(expectedNums), f"k mismatch: got {k}, expected {len(expectedNums)}"

    # Sort only first k elements (like the judge)
    arr[:k] = sorted(arr[:k])

    # expectedNums is already sorted per the prompt, but we can enforce it
    expected_sorted = sorted(expectedNums)

    # Compare only first k elements
    assert arr[:k] == expected_sorted, f"content mismatch: got {arr[:k]}, expected {expected_sorted}"

    return True


# ---------- Example usage with your Solution ----------

class Solution(object):
    def removeElement(self, nums, val):
        # Replace this with the version you want to test
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


def run_all_tests():
    sol = Solution()

    tests = [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 0, 1, 3, 4]),
        ([], 1, []),
        ([1], 1, []),
        ([1], 2, [1]),
    ]

    for idx, (nums, val, expected) in enumerate(tests, 1):
        ok = custom_judge(sol.removeElement, nums, val, expected)
        print(f"Test {idx}: PASS")

run_all_tests()
