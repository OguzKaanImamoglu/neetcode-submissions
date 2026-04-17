# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head

        while fast:
            fast = fast.next
            slow = slow.next

            if fast:
                fast = fast.next
            else:
                return False

            if fast == slow:
                return True

        return False
        