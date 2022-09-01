# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left = tl = ListNode(-1)
        right = tr = ListNode(-1)
        
        cur = head
        
        while cur:
            if cur.val < x:
                tl.next = cur
                tl = tl.next
            else:
                tr.next = cur
                tr = tr.next
            cur = cur.next
            
        tl.next = right.next
        tr.next = None
        
        return left.next
