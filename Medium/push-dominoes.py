class Solution:
    def pushDominoes(self, dominoes: str) -> str:
    
        dom = list(dominoes)
        q = deque()
        
        for i,d in enumerate(dom):
            if d != '.':
                q.append([i,d])
                
        while q:
            index, direction = q.popleft()
            
            if direction == 'L' and index > 0 and dom[index-1] == '.':
                q.append([index-1, 'L'])
                dom[index-1] = 'L'
                
            elif direction == 'R' and index+1 < len(dom) and dom[index+1] == '.':
                if index+2 < len(dom) and dom[index+2] == 'L':
                    q.popleft()
                else:
                    q.append([index+1, 'R'])
                    dom[index+1] = 'R'
                        
        return "".join(dom)
