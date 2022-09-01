"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        st = tail = newHead = Node(0)
        oldToCopy = {}
        second = cur = head
        
        while cur:
            
            tail.next = Node(cur.val)
            tail = tail.next
            oldToCopy[cur] = tail
            cur = cur.next
            
        oldToCopy[None] = None
            
        st = st.next
        while second:
            st.random = oldToCopy[second.random]
            second = second.next
            st = st.next
            
        return newHead.next    
