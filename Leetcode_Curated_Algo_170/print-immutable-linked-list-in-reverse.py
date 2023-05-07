class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def count(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.getNext()
            return cnt
        
        def getHeadNodes(head, step):
            cnt = 0
            ans = []
            while head:
                if cnt % step == 0:
                    ans.append(head)
                head = head.getNext()
                cnt += 1
            return ans
        
        def printReverse(head, step):
            cnt = 0
            st = []
            while head != None and cnt < step:
                st.append(head)
                head = head.getNext()
                cnt += 1
            while st:
                st.pop().printValue()
        
        step = int(sqrt(count(head))) + 1
        headNodes = getHeadNodes(head, step)
        while headNodes:
            printReverse(headNodes.pop(), step)
