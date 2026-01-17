# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        '''
        We divide this solution into 4 parts:
        1. Find whether we have atleast k nodes or not first (for the subparts)
        2. Cut the group of k nodes
        3. Reverse the group of k nodes linked list
        4. Stitch the k nodes back to the linked list
        '''

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        current = head

        while True:
            # 1: Check if there are atleast k nodes left
            kth = current
            count = 1

            # Count the nodes
            while kth and count < k:
                kth = kth.next
                count += 1

            # Not enough k nodes!
            if kth is None:
                break

            next_group_head = kth.next

            # 2: Cut off the group
            kth.next = None

            # 3: Reverse List
            reversed_head = self.reverseList(current)

            # 4: Stitch Back
            prev_group_tail.next = reversed_head
            current.next = next_group_head

            # 5: Move pointers to the next group
            prev_group_tail = current
            current = next_group_head

        return dummy.next

    def reverseList(self, head):

        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

# -------- Helpers for testing --------


def build_linked_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head):
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


def run_tests():
    sol = Solution()

    tests = [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1], 1, [1]),
        ([1, 2], 2, [2, 1]),
        ([1, 2, 3], 2, [2, 1, 3]),
        ([1, 2, 3, 4], 4, [4, 3, 2, 1]),
    ]

    for i, (arr, k, expected) in enumerate(tests, 1):
        head = build_linked_list(arr)
        new_head = sol.reverseKGroup(head, k)
        got = linked_list_to_list(new_head)

        print("Test", i)
        print("  input:   ", arr, "k =", k)
        print("  expected:", expected)
        print("  got:     ", got)
        print("  PASS" if got == expected else "  FAIL")
        print()


if __name__ == "__main__":
    run_tests()
