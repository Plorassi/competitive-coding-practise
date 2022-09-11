class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token not in ["/","+","*","-"]:
                stack.append(int(token))
            else:
                o1,o2 = stack.pop(),stack.pop()
                tmp = 0
                if token == "/":
                    tmp = int(o2/o1)
                elif token == "+":
                    tmp = o2+o1
                elif token == "-":
                    tmp = o2-o1
                else:
                    tmp = o2*o1

                stack.append(tmp)
                
        return stack[0]
