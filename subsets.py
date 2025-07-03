class Solution(object):
    def subsets(self, nums):
        """
        Generate all possible subsets (the power set) of a list of integers.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []  # This will store all subsets we generate

        def backtrack(start, path):
            """
            Recursive helper function to build subsets.

            :param start: The index in nums from which to start including elements
            :param path: The current subset being built (a list)
            """
            # Append a copy of the current subset to the results
            # We use path[:] to ensure we store a snapshot, not a reference
            res.append(path[:])

            # Try adding each of the remaining elements one by one
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])

                # Recursively build the next subset from remaining elements
                backtrack(i + 1, path)

                # Backtrack: remove the last element before trying the next one
                # This step "undoes" the choice to explore a new path
                path.pop()

        # Start the recursion with an empty path and starting index 0
        backtrack(0, [])

        # Return all the collected subsets
        print(res)
        return res


nums1 = [1, 2, 3]
Solution().subsets(nums1)

nums2 = [0]
Solution().subsets(nums2)

nums3 = []
Solution().subsets(nums3)
