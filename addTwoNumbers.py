class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

# Helper functions


def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Testing
l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])
result = Solution().addTwoNumbers(l1, l2)
print(linkedlist_to_list(result))  # [7, 0, 8]

l3 = list_to_linkedlist([0])
l4 = list_to_linkedlist([0])
result = Solution().addTwoNumbers(l3, l4)
print(linkedlist_to_list(result))  # [0]

l5 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
l6 = list_to_linkedlist([9, 9, 9, 9])
result = Solution().addTwoNumbers(l5, l6)
print(linkedlist_to_list(result))  # [8, 9, 9, 9, 0, 0, 0, 1]
