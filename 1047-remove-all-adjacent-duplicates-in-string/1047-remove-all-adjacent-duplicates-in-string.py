class Solution:
    def removeDuplicates(self, s: str) -> str:
        removal_stack = []
        
        #need to remove from stack to make it a 1 pass
        for char in s: 
            if len(removal_stack) > 0: #if there is an element in stack
                if char == removal_stack[-1]: #if the char is the same as the top eleement
                    removal_stack.pop()
                else: 
                    removal_stack.append(char) #add into stack if not the same
            else: 
                removal_stack.append(char) #add to stack if it's not in the stack
        return "".join(removal_stack)
       
        
        