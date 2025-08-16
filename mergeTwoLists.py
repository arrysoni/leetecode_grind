# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        # Dummy node to start the merged list
        dummy = ListNode()
        tail = dummy

        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining nodes
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


# Helper: Convert Python list to Linked List
def list_to_linkedlist(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper: Convert Linked List to Python list


def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ==== TEST CASES ====
s = Solution()

list1 = list_to_linkedlist([1, 2, 4])
list2 = list_to_linkedlist([1, 3, 4])
merged = s.mergeTwoLists(list1, list2)
print(linkedlist_to_list(merged))   # 👉 [1,1,2,3,4,4]

list1 = list_to_linkedlist([])
list2 = list_to_linkedlist([])
merged = s.mergeTwoLists(list1, list2)
print(linkedlist_to_list(merged))   # 👉 []

list1 = list_to_linkedlist([])
list2 = list_to_linkedlist([0])
merged = s.mergeTwoLists(list1, list2)
print(linkedlist_to_list(merged))   # 👉 [0]
