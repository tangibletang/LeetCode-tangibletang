class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result_stack = []
        for element in tokens: 
            if element == "+":
                temp = result_stack[-1] + result_stack [-2]
                result_stack.pop()
                result_stack.pop()
                result_stack.append(temp)
            elif element == "*":
                temp = result_stack[-1] * result_stack [-2]
                result_stack.pop()
                result_stack.pop()
                result_stack.append(temp)
            elif element == "/":
                temp = int(result_stack[-2] / result_stack [-1])
                result_stack.pop()
                result_stack.pop()
                result_stack.append(temp)
            elif element == "-":
                temp = result_stack[-2] - result_stack [-1]
                result_stack.pop()
                result_stack.pop()
                result_stack.append(temp)
            else: #it's a number
                result_stack.append(int(element))
            #print ("element: ", element, " result_stack: ", result_stack)
        return result_stack[-1]