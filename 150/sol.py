from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sign = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t in sign:
                a = int(stack.pop())
                b = int(stack[-1])
                if t == '+':
                        result = a + b
                elif t == '-':
                    result = b -a
                elif t == '*':
                    result = a * b
                elif t == '/':
                    result = int(b / a)
                # print(result)
                stack[-1] = result
            else:
                stack.append(t)

        return int(stack[-1])
    

    
if __name__ == "__main__":
    sol = Solution()
    tokens = ["2","1","+","3","*"]
    tokens2 = ["4","13","5","/","+"]
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(tokens))
    print(sol.evalRPN(tokens2))
    print(sol.evalRPN(tokens3))