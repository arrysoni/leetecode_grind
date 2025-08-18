# Definition for singly-linked list.
import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))

        dummy = ListNode(0)
        cur = dummy

        while h:
            _, i, node = heapq.heappop(h)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))

        return dummy.next


# Helper: Convert list → linked list
def build_linked_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

# Helper: Convert linked list → list


def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


# Example 1
lists = [build_linked_list([1, 4, 5]),
         build_linked_list([1, 3, 4]),
         build_linked_list([2, 6])]

sol = Solution()
result = sol.mergeKLists(lists)
print(to_list(result))  # expected: [1,1,2,3,4,4,5,6]


# Example 2
lists = []
print(to_list(sol.mergeKLists(lists)))  # expected: []

# Example 3
lists = [build_linked_list([])]
print(to_list(sol.mergeKLists(lists)))  # expected: []
