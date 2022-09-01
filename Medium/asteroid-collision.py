class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for i,a in enumerate(asteroids):
            tmp = True
            while (stack and stack[-1] > 0 and a < 0):
                if (abs(stack[-1]) < abs(a)):
                    stack.pop()
                elif (abs(stack[-1]) == abs(a)):
                    stack.pop()
                    tmp = False
                    break
                else:
                    tmp = False
                    break
            if tmp:
                stack.append(a)
                
        return stack
