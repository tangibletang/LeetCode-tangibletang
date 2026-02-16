class Solution:
    def isValid(self, s: str) -> bool:
        bracket_matches = {")":"(", "]":"[", "}":"{"} #dictionary for quick pairings
        stack = [] #stack to add the open brackets

        for char in s: #java style loop
            if char in bracket_matches:
                temp = stack.pop() if stack else '#'
                if bracket_matches[char] == temp:
                    continue
                else: 
                    return False
            else: #not a closed bracket
                stack.append(char)
        return not stack #it would be empty if everything worked out
