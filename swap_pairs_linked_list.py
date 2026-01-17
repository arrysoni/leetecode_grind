# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Dummy node helps handle head swaps cleanly
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Continue while there are at least two nodes to swap
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swap the two nodes by rewiring pointers
            prev.next = second
            first.next = second.next
            second.next = first

            # Move prev to the end of the swapped pair
            prev = first

        return dummy.next


def build_linked_list(values):
    """Convert Python list to linked list"""
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head):
    """Convert linked list back to Python list"""
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


# -------- Test cases --------

def run_tests():
    sol = Solution()

    tests = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),   # Example 1
        ([], []),                       # Example 2
        ([1], [1]),                     # Example 3
        ([1, 2, 3], [2, 1, 3]),         # Example 4
        ([5, 6], [6, 5]),               # Extra
        ([0, 1, 2, 3, 4], [1, 0, 3, 2, 4])  # Extra
    ]

    for i, (inp, expected) in enumerate(tests, 1):
        head = build_linked_list(inp)
        swapped = sol.swapPairs(head)
        output = linked_list_to_list(swapped)

        print(f"Test {i}")
        print("Input:   ", inp)
        print("Output:  ", output)
        print("Expected:", expected)
        print("PASS" if output == expected else "FAIL")
        print()


if __name__ == "__main__":
    run_tests()
