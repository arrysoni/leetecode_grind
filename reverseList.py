class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper: Convert list to linked list


def list_to_linkedlist(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for val in items[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper: Print linked list


def print_linkedlist(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Solution Class


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


# Test cases
s = Solution()

head1 = list_to_linkedlist([1, 2, 3, 4, 5])
reversed1 = s.reverseList(head1)
print_linkedlist(reversed1)

head2 = list_to_linkedlist([1, 2])
reversed2 = s.reverseList(head2)
print_linkedlist(reversed2)

head3 = list_to_linkedlist([])
reversed3 = s.reverseList(head3)
print_linkedlist(reversed3)
