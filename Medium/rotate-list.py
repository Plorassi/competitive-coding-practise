# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head
        
        dummy = tail = head
        l = 0
        
        while tail.next:
            tail = tail.next
            l += 1
            
        l = l+1
        k = k%l
        
        if k == 0:
            return head
        
        k = l-k-1
        
        while k > 0:
            dummy = dummy.next
            k -= 1
            
        tmp = dummy.next
        dummy.next = None
        tail.next = head
        return tmp
            
