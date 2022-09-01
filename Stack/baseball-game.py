class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack = []
        sum_res = 0
        
        for op in ops:
            if op not in ["+","D","C"]:
                stack.append(int(op))
                sum_res += int(op)
            else:
                if op == "+":
                    sum_res += stack[-1]+stack[-2]
                    stack.append(stack[-1]+stack[-2])
                elif op == "D":
                    sum_res += stack[-1]*2
                    stack.append(stack[-1]*2)
                else:
                    x = stack.pop()
                    sum_res -= x

        return sum_res
        
