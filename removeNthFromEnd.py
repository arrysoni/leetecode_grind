# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        first = dummy
        second = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node from end
        second.next = second.next.next

        return dummy.next



head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
new_head = sol.removeNthFromEnd(head, 2)

while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next
